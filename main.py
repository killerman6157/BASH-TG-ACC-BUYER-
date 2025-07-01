
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from dotenv import load_dotenv

from handlers import register_all_handlers
from database import init_db

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)
    init_db()

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    register_all_handlers(dp)
    await bot.set_my_commands([
        BotCommand(command='start', description='Start bot'),
        BotCommand(command='cancel', description='Cancel current operation'),
        BotCommand(command='account_balance', description='Check your account balance'),
        BotCommand(command='withdraw', description='Withdraw your balance'),
        BotCommand(command='language', description='Change language'),
        BotCommand(command='admin', description='Admin stats')
    ])

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
