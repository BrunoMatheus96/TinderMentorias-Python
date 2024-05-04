from fastapi import APIRouter, Depends

from src.auth.AuthDTO import LoginDTO
from src.auth.AuthService import AuthService
from src.user.UserDTO import RegisterDTO
from src.user.UserService import UserService

router = APIRouter()

authService = AuthService()


@router.post('/login', response_description="Rota para logar um novo Usuário.")
async def login_de_usuario(dto: LoginDTO):
    # Retorna o que foi feito no auth.AuthService.py SE os dados enviados forem do tipo ao do auth.dto
    return authService.login(dto)


@router.post('/register',status_code=201, response_description="Rota para criar um novo Usuário.")
async def cadastro_de_usuario(dto: RegisterDTO, userService: UserService = Depends(UserService)):

    return await userService.user_register(dto)
