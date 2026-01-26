from fastapi import APIRouter
from src.backend.app.core.logging import get_logger

logger = get_logger()

router = APIRouter(prefix="/home")

@router.get("/")
def read_root():
    logger.info("Homepage accessed")
    return {"message": "Welcome to the Banking Project"}