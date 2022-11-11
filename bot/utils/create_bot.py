from dotenv import load_dotenv
import os
from aiogram import Bot, types

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    exit("Error: no token provided")
bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
