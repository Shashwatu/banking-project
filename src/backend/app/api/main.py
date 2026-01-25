from fastapi import APIRouter
from .routes.home import router as home_router

router = APIRouter()

router.include_router(home_router)