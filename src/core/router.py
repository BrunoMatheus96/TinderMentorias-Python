from fastapi import APIRouter

from src.core.config import get_settings
from src.core.logger import ApiLogger

router = APIRouter()


@router.get("/ola-mundo")
def read_root():
    settings = get_settings()
    api_logger = ApiLogger()

    api_logger.debug('This is a debug line')
    api_logger.info('This is a info line')
    api_logger.warning('This is a warning line')
    api_logger.error('This is a error line')
    api_logger.critical('This is a critical line')

    return {'message': 'Hello world', 'log_level': settings.LOG_LEVEL}
