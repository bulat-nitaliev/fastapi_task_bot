from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, async_scoped_session, AsyncSession
from asyncio import current_task

from core.config import settings

class DatabaseHelper:
    def __init__(self, url:str, echo:bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=True
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            self.session_factory,
            scopefunc=current_task
        )
        return session
    
    async def session_dependency(self)->AsyncSession:
        session =  self.get_scoped_session() 
        yield session
        await session.remove()

db_helper = DatabaseHelper(
    url=settings.db_url,
    echo=settings.echo
)