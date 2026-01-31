from fastapi import FastAPI
from src.backend.app.core.config import settings
from src.backend.app.api.main import router as api_router
from contextlib import asynccontextmanager
from src.backend.app.core.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title=settings.TITLE, 
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    lifespan=lifespan,
    )

app.include_router(api_router, prefix=settings.API_V1_STR)