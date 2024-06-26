from fastapi import APIRouter

from src.auth.AuthController import router as auth_router
from src.user.UserController import router as user_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth')
router.include_router(user_router, prefix='/user')
