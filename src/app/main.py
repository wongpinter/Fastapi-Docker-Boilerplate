from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.authentication.router import init_auth_router
from app.core.config import settings
from app.core.utils import ping

app = FastAPI(
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_VERSION}/openapi.json"
)

register_tortoise(
    app,
    config=settings.TORTOISE_ORM,
    generate_schemas=True
)

init_auth_router(app)
app.include_router(ping.router)

