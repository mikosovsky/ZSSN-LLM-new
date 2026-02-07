from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class OpenAISettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="OPENAI_", extra="ignore"
    )
    api_key: str
    models: List[str]
    modes: List[str]
