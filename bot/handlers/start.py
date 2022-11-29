import os

from aiogram import Dispatcher, types

from .signup import start_register
from .main import start_menu
from utils.utils import get_data

DB_API_URL = os.getenv('DB_API_URL')


async def cmd_start(message: types.Message):
    """
    Делает get запрос к API,
    переводит на регистрацию или в основное меню
    """
    user_id = message.from_user.id
    try:
        user = await get_data(f'{DB_API_URL}users/{user_id}')
        if user['is_banned'] == False:
            await start_menu(message)
        else:
            await message.answer('Извините, вы не допущены к использованию бота')
    except:
        await start_register(message)


def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start")
