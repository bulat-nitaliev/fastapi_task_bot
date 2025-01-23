from decouple import config
from aiogram import Bot, Dispatcher
import asyncio, logging
from hendler.start import start
from datetime import datetime, date
import pytz     #   pip install pytz


mos = pytz.timezone('Europe/Moscow')
moscow_time = datetime.now(mos)


bot = Bot(token=config('API_TOKEN'))
dp = Dispatcher()



async def main():
    dp.include_router(start)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')