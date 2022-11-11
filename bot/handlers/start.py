from aiogram import Dispatcher, types

from .signup import start_register
from .main import start_menu
from utils.utils import get_data


async def cmd_start(message: types.Message):
    """
    Делает get запрос к API,
    переводит на регистрацию или в основное меню
    """
    user_id = message.from_user.id
    await start_menu(message)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
