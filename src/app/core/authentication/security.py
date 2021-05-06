from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from .users import (
    user_db,
    User,
    UserCreate,
    UserUpdate,
    UserDB
)
from ..config import settings

jwt_authentication = JWTAuthentication(
    secret=settings.SECRET_KEY,
    lifetime_seconds=settings.ACCESS_TOKEN_EXPIRED,
    tokenUrl="/auth/jwt/login"
)

authentication = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
