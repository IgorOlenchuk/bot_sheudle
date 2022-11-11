import os
import logging
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


DB_API_URL = os.getenv('DB_API_URL')

class Form(StatesGroup):
    tg_id = State()
    tg_name = State()


async def start_register(message: types.Message):
    """
    Welcoming user
    """
    await message.reply("Добро пожаловать в\nЧат-бот Sanela Userbot.")



def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(start_register, commands='/start')
