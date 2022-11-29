import os

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup

from utils.utils import get_data, is_time_to_show, patch_data, post_data
from utils.create_bot import bot
from utils.db import get_userbots_list
from keyboards.replykeyboards import keyboard_main_menu, keyboard_cancel, keyboard_main_menu_author, keyboard_cancel_author
from utils.create_bot import bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


DB_API_URL = os.getenv('DB_API_URL')
TELEGRAM_ID = os.getenv('TELEGRAM_CHAT_ID')


cb = CallbackData("id", "day")
cb_answer = CallbackData("id", "question", 'user', 'text')


class SendMessage(StatesGroup):
    message = State()


class SendAnswer(StatesGroup):
    message = State()


class SendGroupMessage(StatesGroup):
    message = State()


async def start_menu(message: types.Message):
    respondents = await get_data(f'{DB_API_URL}users/respondents/')
    author = []
    for id in respondents:
        author.append(id)
    if message.from_user.id in author:
        await message.answer("Привет! Добро пожаловать в главное меню!", reply_markup=keyboard_main_menu_author())
    else:
        await message.answer("Привет! Добро пожаловать в главное меню!", reply_markup=keyboard_main_menu())


async def komitet(message: types.Message):
    await message.answer('Нажмите кнопку <strong>"Написать и отправить"</strong>, введите тест и отправьте его. Либо нажмите "Отмена"', reply_markup=keyboard_cancel())


async def groupmessage(message: types.Message):
    await message.answer('Нажмите кнопку <strong>"Создать и отправить пост"</strong>, введите тест и отправьте его. Либо нажмите "Отмена"', reply_markup=keyboard_cancel_author())


async def sendquestion(message: types.Message):
    await SendMessage.message.set()
    await message.answer('Введите Ваш вопрос/предложение:', reply_markup=types.ReplyKeyboardRemove())


async def sendgroupmess(message: types.Message):
    await SendGroupMessage.message.set()
    await message.answer('Введите текст поста/объявления:', reply_markup=types.ReplyKeyboardRemove())


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    respondents = await get_data(f'{DB_API_URL}users/respondents/')
    author = []
    for id in respondents:
        author.append(id)
    if message.from_user.id in author:
        await message.answer(text="🔙Отмена", reply_markup=keyboard_main_menu_author())
    else:
        await message.answer(text="🔙Отмена", reply_markup=keyboard_main_menu())



async def mainmenu(message: types.Message, state: FSMContext):
    await state.finish()
    respondents = await get_data(f'{DB_API_URL}users/respondents/')
    author = []
    for id in respondents:
        author.append(id)
    if message.from_user.id in author:
        await message.answer(text="🔝Главное меню", reply_markup=keyboard_main_menu_author())
    else:
        await message.answer(text="🔝Главное меню", reply_markup=keyboard_main_menu())


async def resend_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text_message'] = message.text
        answer_btn=types.InlineKeyboardMarkup()
        answer_btn.add(types.InlineKeyboardButton(
            text="Ответить", callback_data=cb_answer.new(question=message.message_id, user=message.from_user.id, text=data['text_message'])
            ))
        await bot.send_message(
            -660238043,
            f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> спрашивает: {data['text_message']}",
            parse_mode='HTML', reply_markup=answer_btn)

        url = f"{DB_API_URL}questions/{message.message_id}/"
        await post_data(url=url, json={
            "tg_name": message.from_user.full_name,
            "question": data['text_message']
        })

    await state.finish()
    await message.answer("Спасибо за ваш вопрос", reply_markup=keyboard_main_menu())


async def resend_group_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text_message'] = message.text
        await bot.send_message(
            -660238043,
            f"<strong>🔔Сообщение от Родительского комитета</strong>:\n {data['text_message']}",
            parse_mode='HTML')
    await state.finish()
    await message.answer("Сообщение отправлено", reply_markup=keyboard_main_menu_author())


async def send_answer(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['text_message'] = message.text

    async with state.proxy() as data:   
        print(data['question'])
        await bot.send_message(data['user'], f"<strong>Ответ на Ваш вопрос:</strong> {data['text_message']}", parse_mode='HTML')
    await state.finish()
    await message.delete()


async def shedule(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
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
    

async def callback_cancel(call: types.CallbackQuery):
    await call.message.delete()
    await call.answer()


async def callback_answer(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = callback_data['question']
        data['user'] = callback_data['user']
        data['text'] = callback_data['user']
    await callback_query.message.answer("Напишите ответ")
    await SendAnswer.message.set()


def register_handlers_menu(dp: Dispatcher):

    dp.register_callback_query_handler(
        callback_answer, cb_answer.filter())

    dp.register_callback_query_handler(
        callback_shedule, cb.filter())

    dp.register_message_handler(resend_group_question, state=SendGroupMessage.message)

    dp.register_message_handler(resend_question, state=SendMessage.message)
  
    dp.register_message_handler(send_answer, state=SendAnswer.message)

    dp.register_message_handler(shedule, Text(
        equals="🗓Расписание", ignore_case=True))

    dp.register_message_handler(komitet, Text(
        equals="✉️Задать вопрос", ignore_case=True))

    dp.register_message_handler(sendquestion, Text(
        equals="✏️Написать и отправить", ignore_case=True))

    dp.register_message_handler(cancel, Text(
        equals="🔙Отмена", ignore_case=True))

    dp.register_message_handler(mainmenu, Text(
        equals="🔝Главное меню", ignore_case=True))

    dp.register_message_handler(groupmessage, Text(
        equals="✉️Написать сообщение в группу", ignore_case=True))

    dp.register_message_handler(sendgroupmess, Text(
        equals="✏️Создать и отправить пост", ignore_case=True))
        


