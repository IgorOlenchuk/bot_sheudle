from aiogram import types


def keyboard_main_menu() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("🗓Расписание")
    button_2 = types.KeyboardButton("✉️Задать вопрос")
    button_3 = types.KeyboardButton("✉️Написать сообщение в группу")
    keyboard.add(button_1)
    keyboard.add(button_2)
    return keyboard


def keyboard_main_menu_author() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("🗓Расписание")
    button_2 = types.KeyboardButton("✉️Написать сообщение в группу")
    keyboard.add(button_1)
    keyboard.add(button_2)
    return keyboard


def keyboard_cancel() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("✏️Написать и отправить")
    button_2 = types.KeyboardButton("🔙Отмена")
    button_3 = types.KeyboardButton("🔝Главное меню")
    keyboard.add(button_1).row(button_2, button_3)
    return keyboard



def keyboard_cancel_author() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("✏️Создать и отправить пост")
    button_2 = types.KeyboardButton("🔙Отмена")
    button_3 = types.KeyboardButton("🔝Главное меню")
    keyboard.add(button_1).row(button_2, button_3)
    return keyboard