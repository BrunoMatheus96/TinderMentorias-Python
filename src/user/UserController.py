import os
from datetime import datetime

from fastapi import APIRouter, Depends, Header, HTTPException
from src.auth.AuthService import AuthService
from src.core.middlewares.JWTMiddleware import check_token
from src.user.UserDTO import UpdateUserDTO
from src.user.UserService import UserService

router = APIRouter()

user = UserService()
authService = AuthService()
userService = UserService()


@router.put('/upload_user', dependencies=[Depends(check_token)], tags=['Usuários'])
async def atualizar_dados_do_usuario(authorization: str = Header(default=''),
                                     update_user: UpdateUserDTO = Depends(UpdateUserDTO)):
    try:
        user_logged = await authService.search_user_logged(authorization)

        if not ('.jpg' in update_user.photo.filename or '.jpeg' in update_user.photo.filename or '.png' in update_user.photo.filename):
            raise HTTPException(400, 'Formato do arquivo incorreto')

        photo_path = f'photo-{datetime.now().strftime("%d%m%y%H%M%S")}.jpg'

        with open(photo_path, 'wb+') as photo_file:
            photo_file.write(update_user.photo.file.read())

        result = await userService.update_user(user_logged.id, update_user, photo_path)

        os.remove(photo_path)

        return result

    except Exception as e:
        raise e

