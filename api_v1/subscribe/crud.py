
from ..products.crud import create_or_update_product
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product

from sqlalchemy import select



async def hello(articul:str)->None:
    print(f'hello {articul}')

# async def subscribe(
#         artikul:str, 
#         product: Product,
#         session:AsyncSession,
#         url:str
# ):
#     product = select(Product).where(Product.articul==artikul)

#     return await scheduler.add_job(
#         func=create_or_update_product, 
#         args=(
#             session,
#             artikul,
#             url,
#             product,
#         ),
#         trigger='interval',
#         id=artikul,
#         minutes=2,
#         ) 
        