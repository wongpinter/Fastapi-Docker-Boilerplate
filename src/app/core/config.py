import secrets
from typing import Dict

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Boiler bro"
    API_VERSION: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRED: int = 60 * 4 * 8
    TORTOISE_ORM: Dict = {
        "connections": {
            "default": 'sqlite://./test.db'
        },
        "apps": {
            "models": {
                "models": [
                    "app.core.authentication.users"
                ],
                "default_connection": "default",
            },
        },

    }


settings = Settings()
