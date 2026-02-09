from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache



class Settings(BaseSettings):

    app_name: str = "Autonomous Incident Commander"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow"
    )

    OPENAI_API_KEY: str

@lru_cache
def get_settings() -> Settings:
    return Settings()