from fastapi import APIRouter
from src.auth.AuthController import router as auth_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth')