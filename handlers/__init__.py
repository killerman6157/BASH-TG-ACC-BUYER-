from .otp_handler import router as otp
from .cancel_handler import router as cancel
from .balance_handler import router as balance
from .withdraw_handler import router as withdraw
from .language_handler import router as lang
from .admin_handler import router as admin

def register_all_handlers(dp):
    dp.include_router(otp)
    dp.include_router(cancel)
    dp.include_router(balance)
    dp.include_router(withdraw)
    dp.include_router(lang)
    dp.include_router(admin)
