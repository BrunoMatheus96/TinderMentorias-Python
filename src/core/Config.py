from functools import lru_cache

from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    #Caso o LOG_LEVEL não esteja definido dentro do .env ele vai utilizar o valo 'info'
    LOG_LEVEL: str = "info"


class Config:
    env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
