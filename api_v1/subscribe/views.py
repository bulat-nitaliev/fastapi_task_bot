from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .crud import start_scheduler
from core.models import db_helper
from core.config import settings


router = APIRouter(tags=['Subscribe'])

@router.get('/{artikul}')
async def get_subscribe(artikul:str, session:AsyncSession = Depends(db_helper.session_dependency)):
    url:str = settings.url_get_product_by_articul
    await start_scheduler(artikul, session, url)
    return {'message': f'data update started - {artikul}'}



