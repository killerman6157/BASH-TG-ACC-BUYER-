
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from messages import MESSAGES
from database import get_user

router = Router()

class WithdrawState(StatesGroup):
    choosing_method = State()
    waiting_details = State()

@router.message(F.text == "/withdraw")
async def withdraw(msg: Message, state: FSMContext):
    lang = get_user(msg.from_user.id)[4]
    await msg.answer(MESSAGES[lang]['withdraw_method'])
    await state.set_state(WithdrawState.choosing_method)

@router.message(WithdrawState.choosing_method)
async def choose_method(msg: Message, state: FSMContext):
    await state.update_data(method=msg.text.strip())
    lang = get_user(msg.from_user.id)[4]
    await msg.answer(MESSAGES[lang]['send_account'])
    await state.set_state(WithdrawState.waiting_details)

@router.message(WithdrawState.waiting_details)
async def receive_details(msg: Message, state: FSMContext):
    lang = get_user(msg.from_user.id)[4]
    await msg.answer(MESSAGES[lang]['withdraw_done'])
    await state.clear()
