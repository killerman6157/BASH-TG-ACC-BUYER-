
from aiogram import Router, F
from aiogram.types import Message
from database import get_user
from messages import MESSAGES

router = Router()

@router.message(F.text == "/account_balance")
async def account_balance(msg: Message):
    user = get_user(msg.from_user.id)
    lang = user[4]
    txt = MESSAGES[lang]['balance'].format(user=user[0], v=user[1], u=user[2], bal=user[3])
    await msg.answer(txt)
