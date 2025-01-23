from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    api_v1_prefix:str = '/api/v1'
    db_url: str = 'postgresql+asyncpg://postgres:postgres@localhost/test_db' #f'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'
    echo: bool = True
    url_get_product_by_articul:str = 'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm='
    timeout:int = 30

settings = Settings()
