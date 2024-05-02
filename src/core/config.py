
from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    #Caso o LOG_LEVEL nãoo esteja definido dentro do .env ele vai utilizar o valo 'info'
    log_level: str = "info"


class Config:
    env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
