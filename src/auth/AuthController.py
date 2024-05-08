import os
from datetime import datetime

from fastapi import APIRouter, Body, UploadFile, Depends

from src.auth.AuthDTO import LoginDTO
from src.auth.AuthService import AuthService
from src.user.UserDTO import RegisterDTO
from src.user.UserService import UserService

router = APIRouter()

authService = AuthService()
userService = UserService()


@router.post('/login', responses={401: {"Model": "Message"}})
async def login_de_usuario(login_dto: LoginDTO = Body(...)):
    result = await authService.login(login_dto)

    # Retorna o que foi feito no auth.AuthService.py SE os dados enviados forem do tipo ao do auth.dto
    return result


@router.post('/register', status_code=201, responses={400: {"Model": "Message"}})
async def cadastro_de_usuario(file: UploadFile, register_dto: RegisterDTO = Depends(RegisterDTO)):
    try:
        photo_path = f'src/files/photo-{datetime.now().strftime("%H%M%S")}.jpg'

        with open(photo_path, 'wb+') as photo_file:
            photo_file.write(file.file.read())

        result = await userService.user_register(register_dto, photo_path)

        os.remove(photo_path)

        return result

    except Exception as e:
        raise e
