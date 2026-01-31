from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
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
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = "banking_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

settings = Settings()