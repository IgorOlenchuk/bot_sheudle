from aiogram import types


def keyboard_main_menu(item_list):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for item in item_list:
        buttons.append(item)
    keyboard.add(*buttons)
    return keyboard
