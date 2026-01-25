from fastapi import FastAPI
from src.backend.app.core.config import settings
from src.backend.app.api.main import router as api_router

app = FastAPI(title=settings.TITLE, 
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    )

app.include_router(api_router, prefix=settings.API_V1_STR)