from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from contextlib import asynccontextmanager
from api_v1 import router as router_v1
from core.config import settings
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tasks.task import hello


scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app:FastAPI): 
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    yield
    # try:
    #     scheduler.add_job(
    #         func=hello,
    #         trigger=IntervalTrigger(seconds=10),
    #         id='currency_update_job',
    #         replace_existing=True,
    #         args=('Bulat',)
    #         )
    #     scheduler.start()
    #     print('start')
    #     yield
    # except Exception as e:
    #     print(f"Ошибка инициализации планировщика: {e}")
    # finally:
    #     # Завершение работы планировщика
    #     scheduler.shutdown()
    #     print("Планировщик обновления курсов валют остановлен")


app = FastAPI(lifespan=lifespan)



app.include_router(router_v1, prefix=settings.api_v1_prefix)




if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
