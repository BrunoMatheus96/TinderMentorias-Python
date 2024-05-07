from fastapi import APIRouter, Body, HTTPException

from src.auth.AuthDTO import LoginDTO
from src.auth.AuthService import AuthService
from src.user.UserDTO import RegisterDTO
from src.user.UserService import UserService

router = APIRouter()

authService = AuthService()
userService = UserService()

@router.post('/login', response_description="Rota para logar um novo Usuário.")
async def login_de_usuario(login_dto: LoginDTO = Body(...)):
    result = await authService.login(login_dto)

    if not result.status == 200:
        raise HTTPException(status_code=result.status, detail=result.mensagem)

    del result.dados.password

    token = authService.create_token_jwt(result.dados.id)

    result.dados.token = token

    # Retorna o que foi feito no auth.AuthService.py SE os dados enviados forem do tipo ao do auth.dto
    return result


@router.post('/register', status_code=201, response_description="Rota para criar um novo Usuário.")
async def cadastro_de_usuario(register_dto: RegisterDTO = Body(...)):
    return await userService.user_register(register_dto)
