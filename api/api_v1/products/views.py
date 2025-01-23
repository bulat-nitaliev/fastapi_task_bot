from fastapi import APIRouter, status, Depends, Body
from . import crud
from .shemas import Product, Artikul
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from typing import Annotated
from core.config import settings

router = APIRouter(tags=['Product'])

@router.get('/', response_model=list[Product])
async def get_products(session:AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)
    


@router.post('/',response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    articul: Artikul,
    session:AsyncSession = Depends(db_helper.session_dependency)
                         ):
    url:str = settings.url_get_product_by_articul
    return await crud.create_or_update_product(
        session=session,
        articul=articul,
        url=url
        )
