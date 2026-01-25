from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class Settings(BaseSettings):
    ENVIRONMENT: Literal["local", "staging","production"] = "local"

    model_config = SettingsConfigDict(
        env_file = "../../.env",
        env_ignore_empty = True,
        extra = "ignore"
    )
    API_V1_STR: str = ""
    SITE_NAME: str = ""
    DESCRIPTION: str = ""
    TITLE: str = ""

settings = Settings()