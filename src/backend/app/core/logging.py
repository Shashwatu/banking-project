import os
from loguru import logger
from app.core.config import settings

logger.remove()

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

LOF_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

logger.add(
    sink=os.path.join(LOG_DIR, "debug.log"),
    format=LOG_FORMAT,
    level="DEBUG" if settings.ENVIRONMENT == "local" else "INFO",
    filter=lambda record: record["level"].no <= logger.level("WARNING").no,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
)

logger.add(
    sink=os.path.join(LOG_DIR, "error.log"),
    format=LOG_FORMAT,
    level="ERROR",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    backtrace=True,
    diagnose=True,
)

def get_logger():
    return logger