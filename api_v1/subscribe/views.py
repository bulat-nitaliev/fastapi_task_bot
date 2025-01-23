from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.config import settings
from tasks import scheduler
from .crud import hello


router = APIRouter(tags=['Subscribe'])


# @router.get('/{artikul}')
# async def get_subscribe(
#     product:Product,
#                         artikul:str , 
                            
#                             session:AsyncSession = Depends(db_helper.session_dependency)):
#     url:str = settings.url_get_product_by_articul
    # await create_or_update_product.delay(
    #     session=session,
    #     articul=artikul,
    #     product=product,
    #     url=url
    # )

@router.get('/{artikul}')
async def get_subscribe(
    artikul:str, 
    session:AsyncSession = Depends(db_helper.session_dependency)):
    scheduler.add_job(func=hello, args=(artikul), id=artikul, trigger='interval', seconds=5)
    return {'message': f'data update started - {artikul}'}



