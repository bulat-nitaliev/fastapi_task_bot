from pydantic import BaseModel,ConfigDict
from datetime import datetime


class Artikul(BaseModel):
    artikul: str

class ProductBase(BaseModel):
    name: str
    articul: str
    price: int
    rating: int
    total_quantity:int
    last_date: datetime

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass



class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int