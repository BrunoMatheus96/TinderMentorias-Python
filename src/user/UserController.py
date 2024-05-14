from fastapi import APIRouter, Depends, Header
from src.auth.AuthService import AuthService
from src.core.middlewares.JWTMiddleware import check_token
from src.user.UserDTO import UpdateUserDTO
from src.user.UserService import UserService

router = APIRouter()

user = UserService()
authService = AuthService()
userService = UserService()


@router.put('/upload_user', dependencies=[Depends(check_token)], tags=['Usuários'])
async def atualizar_dados_do_usuario(authorization: str = Header(default=''), update_user: UpdateUserDTO = Depends(UpdateUserDTO)):

    user_logged = await authService.search_user_logged(authorization)
    result = await userService.update_user(user_logged.id, update_user)

    return result
