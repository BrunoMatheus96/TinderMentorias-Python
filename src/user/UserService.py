from fastapi import HTTPException

from src.user.UserDTO import RegisterDTO
from src.user.UserModel import UserModel
from src.user.UserRepository import UserRepository

userRepository = UserRepository()


class UserService:
    async def user_register(self, dto: RegisterDTO) -> object:

        user = UserModel(
            name=dto.name,
            lastName=dto.lastName,
            email=dto.email,
            cep=dto.cep,
            password=dto.password,
            position=dto.position,
            skills=dto.skills,
            photo=dto.photo
        )

        try:
            user_found = await userRepository.search_for_user_by_email(user.email)

            print(user.email)

            if user_found:

                return HTTPException(status_code=400, detail=f'Email {user.email} já cadastrado no sistema')
            else:

                await userRepository.create_user(user)

                return HTTPException(status_code=201, detail='Cadastro realizado com sucesso!')

        except Exception as e:
            print(e)

            return HTTPException(status_code=500, detail="Erro interno no servidor")
