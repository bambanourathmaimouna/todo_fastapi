from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Field


class settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
    DATABASE_URL :  str


settings = settings()