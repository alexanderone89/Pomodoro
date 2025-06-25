from fastapi import APIRouter

from settings import Settings

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/db")
async def ping_db():
    setting = Settings()
    return {'message': setting.GOOGLE_TOKEN_ID}


@router.get("/app")
async def ping_app():
    return {"message": "app is working"}