import os

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData

from utils.utils import get_data, is_time_to_show, patch_data, post_data
from utils.create_bot import bot
from utils.db import get_userbots_list
from keyboards.replykeyboards import keyboard_main_menu


DB_API_URL = os.getenv('DB_API_URL')
TELEGRAM_ID = os.getenv('TELEGRAM_CHAT_ID')

cb = CallbackData("id", "day")

BUTTONS = ["Расписание"]


class SendMessage(StatesGroup):
    message = State()


async def start_menu(message: types.Message):
    """
    Main menu entry point
    """
    keyboard = keyboard_main_menu(BUTTONS)
    await message.answer("Привет! Добро пожаловать в главное меню!", reply_markup=keyboard)


async def shedule(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    days = await get_data(f'{DB_API_URL}days/')
    DAYS = {'Mn': 'Понедельник', 'Tu': 'Вторник', 'We': 'Среда', 'Th': 'Четверг', 'Fr': 'Пятница'}
    for key, value in DAYS.items():
        keyboard.add(types.InlineKeyboardButton(
            text=f"{value}", callback_data=cb.new(day=key)
            )
        )

    await message.answer("Посмотреть расписание на:", reply_markup=keyboard)


async def callback_shedule(callback_query: types.CallbackQuery, callback_data: dict):
    message = '⏱{time_from} - {time_to}🔹 <strong>{lesson}</strong>'
    mesadd = '⏱{time_from} - {time_to}▫️ {lesson}'
    keyboard = types.InlineKeyboardMarkup()
    data = callback_data
    user_id = callback_query.from_user.id
    days_list = await get_data(f'{DB_API_URL}days/{data["day"]}/lessons/')
    if data["day"] == 'Mn':
        a = 'Понедельник'
    if data["day"] == 'Tu':
        a = 'Вторник'
    if data["day"] == 'We':
        a = 'Среду'
    if data["day"] == 'Th':
        a = 'Четверг'
    if data["day"] == 'Fr':
        a = 'Пятницу'
    await callback_query.message.delete()
    await bot.send_message(user_id, text=f'🗓Расписание на <strong>{a}</strong>')
    for day in days_list:
        lesson = str()
        lesson = lesson.join(day['lesson'].split(',')[-3])
        add = str()
        add = add.join(day['lesson'].split(',')[-1])
        if add != "доп.":
            await bot.send_message(user_id, text=message.format(time_from=day['time_from'][:-3], time_to=day['time_to'][:-3], lesson=lesson))
        else:
            await bot.send_message(user_id, text=mesadd.format(time_from=day['time_from'][:-3], time_to=day['time_to'][:-3], lesson=lesson))
    


def register_handlers_menu(dp: Dispatcher):

    dp.register_message_handler(shedule, Text(
        equals="Расписание", ignore_case=True))

    dp.register_callback_query_handler(
        callback_shedule, cb.filter())
