from fastapi import Request

from .security import jwt_authentication, authentication
from .users import UserDB
from ..config import settings


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


def on_after_forgot_password(user: UserDB, token: str, request: Request):
    print(f"User {user.id} has forgot their password. Reset token: {token}")


def after_verification_request(user: UserDB, token: str, request: Request):
    print(f"Verification requested for user {user.id}. Verification token: {token}")


def init_auth_router(app):
    app.include_router(
        authentication.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
    )
    app.include_router(
        authentication.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
    )
    app.include_router(
        authentication.get_reset_password_router(
            settings.SECRET_KEY, after_forgot_password=on_after_forgot_password
        ),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(
        authentication.get_verify_router(
            settings.SECRET_KEY, after_verification_request=after_verification_request
        ),
        prefix="/auth",
        tags=["auth"],
    )
    app.include_router(authentication.get_users_router(), prefix="/users", tags=["users"])
