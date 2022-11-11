import aiohttp
import logging
import os
from dotenv import load_dotenv

load_dotenv()

DB_API_URL = os.getenv('DB_API_URL')


async def get_activities_list(url):
    """Запрашивает список мероприятий."""
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            logging.info('get db data success')
            return await resp.json()
    except Exception as error:
        err_message = 'get db data error', error
        raise Exception(err_message)


async def get_activitiy_detail(url):
    """Запрашивает данные мероприятия из базы."""
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            logging.info('get db data success')
            return await resp.json()
    except Exception as error:
        err_message = 'get db data error', error
        raise Exception(err_message)


async def get_userbots_list(url):
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            logging.info('get db data success')
            return await resp.json()
    except Exception as error:
        err_message = 'get db data error', error
        raise Exception(err_message)


async def get_userbots_detail(url):
    """Запрашивает данные мероприятия из базы."""
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            logging.info('get db data success')
            return await resp.json()
    except Exception as error:
        err_message = 'get db data error', error
        raise Exception(err_message)



async def get_speakers_list(url):
    """Запрашивает список мероприятий."""
    try:
        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            logging.info('get db data success')
            return await resp.json()
    except Exception as error:
        err_message = 'get db data error', error
        raise Exception(err_message)