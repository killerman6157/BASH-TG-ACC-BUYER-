
from aiogram import Router, F, types
import os
from database import get_stats

router = Router()
ADMIN_ID = int(os.getenv("ADMIN_ID"))

@router.message(F.text == "/admin")
async def admin_panel(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return await msg.answer("Access denied.")
    users, verified, unverified = get_stats()
    await msg.answer(f"👥 Users: {users}\n✅ Verified: {verified}\n❌ Unverified: {unverified}")
