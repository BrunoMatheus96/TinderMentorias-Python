import time

import jwt
from decouple import config
from fastapi import HTTPException

from src.auth.AuthDTO import LoginDTO
from src.core.util.AuthUtil import AuthUtil
from src.core.util.ResponseDTO import ResponseDTO
from src.user.UserModel import UserModel
from src.user.UserRepository import UserRepository
from src.user.UserService import UserService

JWT_SECRET = config('JWT_SECRET')

userRepository = UserRepository()

authUtil = AuthUtil()

userService = UserService()


class AuthService:

    def create_token_jwt(self, user_id: str) -> str:
        payload = {
            "user_id": user_id,
            #"expiration_time": time.time() + 6000 -> Faz com que o tokem mude sempre
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

        return token

    def decode_token_jwt(self, token: str):
        try:
            token_decoded = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            return token_decoded

        except Exception as e:
            print(e)
            return None

    async def login(self, login_dto: LoginDTO):
        user_found = await userRepository.search_for_user_by_email(login_dto.login)
        print(user_found)

        if not user_found:
            raise HTTPException(401, 'Dados inválidos ou não cadastrados')
        else:
            if authUtil.check_password(login_dto.password, user_found.password):
                token = self.create_token_jwt(user_found.id)
                return ResponseDTO('Login realizado com sucesso', token, 200)
            else:
                raise HTTPException(401, 'Dados inválidos')

    async def search_user_logged(self, authorization: str) -> UserModel:
        token = authorization.split(' ')[1]
        payload = self.decode_token_jwt(token)

        registered_user = await userService.find_user(payload['user_id'])

        user_logged = registered_user.dados

        return user_logged
