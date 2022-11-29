import os
import logging
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from .main import start_menu
from utils.utils import post_data


DB_API_URL = os.getenv('DB_API_URL')


class Form(StatesGroup):
    number = State()
    tg_id = State()
    tg_name = State()
    first_name = State()
    last_name = State()


async def start_register(message: types.Message):
    """
    Welcoming user
    """
    await Form.number.set()

    await message.reply('Добро пожаловать в\nЧат-бот Родительский комитет 1 "В"')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_phone_request = types.KeyboardButton(
        text='Предоставить', request_contact=True)
    keyboard.add(btn_phone_request)
    await message.answer("Предоставьте свой номер телефона", reply_markup=keyboard)


async def process_number(message: types.Message, state: FSMContext):
    """
    Process user phone number
    """
    if message.content_type == 'contact':
        async with state.proxy() as data:
            data['number'] = message.contact.phone_number

        await Form.tg_id.set()
        async with state.proxy() as data:
            data['tg_id'] = message.from_user.id
        await Form.tg_name.set()
        async with state.proxy() as data:
            data['tg_name'] = message.from_user.first_name
        await Form.first_name.set()
        await message.answer("Введите имя:", reply_markup=types.ReplyKeyboardRemove())
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_phone_request = types.KeyboardButton(
            text='Предоставить', request_contact=True)
        keyboard.add(btn_phone_request)
        await message.answer("Для предоставления номера телефона нажмите кнопку \"Предоставить\"", reply_markup=keyboard)


async def process_first_name(message: types.Message, state: FSMContext):
    """
    Process user first name
    """
    async with state.proxy() as data:
        data['first_name'] = message.text

    await Form.last_name.set()
    await message.answer("Введите фамилию:")


async def process_last_name(message: types.Message, state: FSMContext):
    """
    Process user last name
    """
    async with state.proxy() as data:
        data['last_name'] = message.text

    async with state.proxy() as data:
        url = f'{DB_API_URL}users/'
        await post_data(url=url, json={
            "id": data['tg_id'],
            "tg_name": data['tg_name'],
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "number": data['number']
        })

    await state.finish()

    await message.answer('Ура! Здорово, что Вы с нами! Здесь мы собрали важную информацию')

    await start_menu(message)


async def cancel(message: types.Message, state: FSMContext):
    """
    Allows user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        logging.info('Here', current_state)
        return

    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


def register_handlers_registration(dp: Dispatcher):
    dp.register_message_handler(start_register, commands='/start')
    dp.register_message_handler(process_first_name, state=Form.first_name)
    dp.register_message_handler(process_last_name, state=Form.last_name)
    dp.register_message_handler(
        process_number, state=Form.number, content_types='contact')
    dp.register_message_handler(
        process_number, state=Form.number)
    dp.register_message_handler(cancel, commands="cancel", state='*')