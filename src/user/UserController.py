from fastapi import APIRouter, Depends, Header

from src.auth.AuthService import AuthService
from src.core.middlewares.JWTMiddleware import check_token
from src.user.UserService import UserService

router = APIRouter()

user = UserService()
authService = AuthService()
userService = UserService()


@router.put('/upload_user', dependencies=[Depends(check_token)], tags=['Usuários'])
async def atualizar_dados_do_usuario():

    return 'Ta funcionando'
