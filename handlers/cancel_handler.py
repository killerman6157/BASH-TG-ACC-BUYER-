
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from messages import MESSAGES
from database import get_user

router = Router()

@router.message(F.text == "/cancel")
async def cancel(msg: types.Message, state: FSMContext):
    await state.clear()
    lang = get_user(msg.from_user.id)[4]
    await msg.answer(MESSAGES[lang]['cancel'])
