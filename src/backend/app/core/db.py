from typing import AsyncGenerator
from src.backend.app.core.config import settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.backend.app.core.logging import get_logger

logger = get_logger()

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Error getting session: {e}")
            await session.rollback()
            raise e
        finally:
            await session.close()

async def init_db():
    pass