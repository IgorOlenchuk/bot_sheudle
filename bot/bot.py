import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.create_bot import bot
from handlers.start import register_handlers_start
from handlers.signup import register_handlers_registration
from handlers.main import register_handlers_menu
from logging.handlers import RotatingFileHandler


logging.basicConfig(
        level=logging.DEBUG,
        filename='program.log',
        format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Указываем обработчик логов
handler = RotatingFileHandler(
    'my_logger.log',
    maxBytes=50000000,
    backupCount=5)
logger.addHandler(handler)
logger.debug('123')
logger.info('Сообщение отправлено')
logger.warning('Большая нагрузка!')
logger.error('Бот не смог отправить сообщение')
logger.critical('Всё упало! Зовите админа!1!111')


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Для начала работы"),
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    # Объявление и инициализация объектов бота и диспетчера
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    Dispatcher.set_current(dp)
    # Регистрация хэндлеров
    register_handlers_start(dp)
    register_handlers_menu(dp)
    register_handlers_registration(dp)

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
