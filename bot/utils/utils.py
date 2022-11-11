import aiohttp
from utils.create_bot import bot
from datetime import datetime
import pytz


async def get_data(url):
    """Делает запрос к API."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    except Exception as error:
        raise Exception(error)


async def post_data(url, json):
    """
    Makes post request to the database
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with aiohttp.ClientSession() as session:
                await session.post(url=url, json=json)

    except Exception as error:
        raise Exception(error)


async def patch_data(url, json):
    """
    Makes post request to the database
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with aiohttp.ClientSession() as session:
                await session.patch(url=url, json=json)

    except Exception as error:
        raise Exception(error)


async def push_message_all(message_to_send):
    id_list = await get_data('http://127.0.0.1:8000/api/users/ids/')
    for id in id_list:
        await bot.send_message(id, message_to_send)


def is_time_to_show(time):
    month, day = str(time[5:10]).split('-')
    hour, minute = str(time[11:16]).split(':')
    current_month, current_day, current_hour, current_minute = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime("%m-%d-%H-%M").split('-')
    if current_month > month:
        return True
    if current_month == month and current_day > day:
        return True
    if current_month == month and current_day == day and current_hour > hour:
        return True
    if current_month == month and current_day == day and current_hour == hour and current_minute >= minute:
        return True
    return False


def is_time_to_send(time, max_delivery_gap):
    month, day = str(time[5:10]).split('-')
    hour, minute = str(time[11:16]).split(':')
    current_month, current_day, current_hour, current_minute = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime("%m-%d-%H-%M").split('-')
    if current_day == day and current_month == month and current_hour == hour:
        delivery_gap = int(minute) - int(current_minute)
        if delivery_gap <= 0 and delivery_gap > -max_delivery_gap:
            return True
    return False


async def send_photo_or_text(user_id, image, message):
    if image != None:
        await bot.send_photo(user_id, photo=(open(f"../bootcamp{image}", 'rb')), caption=message, parse_mode='HTML')
    else:
        if message != '':
            await bot.send_message(user_id, text=message, parse_mode='HTML')
