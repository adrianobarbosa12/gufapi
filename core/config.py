from typing import List
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = ''
    DBBaseModel = declarative_base

    JWT_SECRET: str = '52jL6bx7EMaaQH--PuI7Dr607C_8S1RNHkuJTviKG-I'
    ALGORITHM: str = 'H5256'

    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
