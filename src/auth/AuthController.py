import os
from datetime import datetime

from fastapi import APIRouter, Body, UploadFile, Depends, HTTPException

from src.auth.AuthDTO import LoginDTO
from src.auth.AuthService import AuthService
from src.user.UserDTO import RegisterDTO
from src.user.UserService import UserService

router = APIRouter()

authService = AuthService()
userService = UserService()


@router.post('/login', responses={
    200: {"model": str, "description": "Login realizado com sucesso",
          "content": {"application/json": {"example": {"detail": "string", "dados": "string", "status": 200}}}},
    401: {"model": str, "description": "Usuário não autorizado",
          "content": {"application/json": {"example": {"detail": "string"}}}}
})
async def login_de_usuario(login_dto: LoginDTO = Body(...)):
    result = await authService.login(login_dto)

    # Retorna o que foi feito no auth.AuthService.py SE os dados enviados forem do tipo ao do auth.dto
    return result


@router.post('/register', status_code=201, responses={
    201: {"model": str, "description": "Login realizado com sucesso",
          "content": {"application/json": {"example": {"detail": "string"}}}},
    400: {"model": str, "description": "Usuário não autorizado",
          "content": {"application/json": {"example": {"detail": "string"}}}}
})
async def cadastro_de_usuario(file: UploadFile, register_dto: RegisterDTO = Depends(RegisterDTO)):
    try:
        print(file)
        print('.jpg' in file.filename)

        if not ('.jpg' in file.filename or '.jpeg' in file.filename or '.png' in file.filename):
            raise HTTPException(400, 'Formato do arquivo incorreto')

        photo_path = f'src/files/photo-{datetime.now().strftime("%d%m%y%H%M%S")}.jpg'

        with open(photo_path, 'wb+') as photo_file:
            photo_file.write(file.file.read())

        result = await userService.user_register(register_dto, photo_path)

        os.remove(photo_path)

        return result

    except Exception as e:
        raise e
