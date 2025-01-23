from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from sqlalchemy import select, Result, update
from .dependencies import get_product_by_articul
from .shemas import Artikul




async def create_or_update_product(
                            session: AsyncSession, 
                            articul:Artikul, 
                            url:str,
                            )->Product:
    data = await get_product_by_articul(
        articul=articul.artikul,
        url=url
    )

    stat = await session.execute(select(Product).where(Product.articul==articul.artikul))
    if prod:= stat.fetchone():
        id = [p.id for p in prod][0]
        stmt = update(Product).where(Product.articul==articul.artikul).values(**data)
        await session.execute(stmt)
        await session.commit()
        return await session.get(Product, id)
    
    prod = Product(**data)
    session.add(prod)
    await session.commit()
    return prod


async def get_products(session:AsyncSession)->list[Product]:
    stat = select(Product).order_by(Product.id)
    result:Result = await session.execute(stat)
    products = result.scalars().all()
    return list(products)

