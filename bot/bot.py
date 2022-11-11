import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.create_bot import bot
from handlers.start import register_handlers_start
from handlers.main import register_handlers_menu
from logging.handlers import RotatingFileHandler


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="this is the entrypoint"),
    ]
    await bot.set_my_commands(commands)


async def main():
    # Объявление и инициализация объектов бота и диспетчера
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    Dispatcher.set_current(dp)
    # Регистрация хэндлеров
    register_handlers_start(dp)
    register_handlers_menu(dp)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    # await dp.skip_updates()  # пропуск накопившихся апдейтов (необязательно)
    await dp.start_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()
    # asyncio.run(main())
