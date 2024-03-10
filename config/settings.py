"""Setting"""

import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """Setting"""
    API_KEY: str

@lru_cache()
def get_settings():
    """Get setting"""
    enviromment = os.getenv('ENVIRONMENT', 'local')
    if enviromment == 'local':
        return Settings(_env_file='.env', _env_file_encoding='utf-8')
    return Settings()