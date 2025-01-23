from fastapi import  status, HTTPException
import aiohttp
from datetime import datetime




async def get_product_by_articul(articul:int , url:str)->dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{url}{articul}') as response:
            if response.status == 200:
                data = await response.json()
                if data['data']['products']:
                    return {
                    'name': data['data']['products'][0]['name'],
                    'articul': articul,
                    'price': data['data']['products'][0]['priceU'],
                    'rating': data['data']['products'][0]['rating'],
                    'total_quantity': data['data']['products'][0]['totalQuantity'],
                    'last_date': datetime.now()
                    }
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'product by articul {articul} not found'
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'product by articul {articul} not found'
            )
