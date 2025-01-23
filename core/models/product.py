from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime

class Product(Base):
    name: Mapped[str]
    articul: Mapped[str] = mapped_column(index=True, unique=True)
    price: Mapped[int]
    rating: Mapped[int]
    total_quantity:Mapped[int]
    last_date: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.now, server_default=func.now())


       