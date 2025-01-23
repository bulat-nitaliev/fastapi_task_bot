
from ..products.crud import create_or_update_product
from sqlalchemy.ext.asyncio import AsyncSession
from core.config import settings
from ..products.shemas import Artikul 
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from sqlalchemy import select



async def start_scheduler(artikul:str, session:AsyncSession, url:str)->None:
    art = Artikul(artikul=artikul)
    # jobstores = {
    #     'default': SQLAlchemyJobStore(settings.db_url)
    # }
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        func=create_or_update_product,
        trigger=IntervalTrigger(minutes=settings.timeout),
        id=artikul,
        replace_existing=True,
        args=(
            session,
            art,
            url
        ),
    )
    scheduler.start()
    print(f'start scheduler')
