import os

from fastapi import HTTPException
from src.user.UserDTO import RegisterDTO
from src.user.UserRepository import UserRepository
from src.auth.providers.AWSProvider import AWSProvider
from src.core.util.ConverterUtil import ConverterUtil

userRepository = UserRepository()

awsProvider = AWSProvider()


class UserService:
    async def user_register(self, user: RegisterDTO, photo_path):

        # Validações da senha DTO
        special_characters = "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~"
        has_special_char = any(char in special_characters for char in user.password)
        has_digit = any(char.isdigit() for char in user.password)
        if not has_special_char or not has_digit:
            raise HTTPException(status_code=400, detail="A senha deve conter letra, número e caracter especial")

        try:
            user_found = await userRepository.search_for_user_by_email(user.email)

            if user_found:
                print(user_found)
                os.remove(photo_path)
                raise HTTPException(status_code=400, detail=f'O email {user.email} já está cadastrado no sistema')
            else:

                id_user = ConverterUtil.user_converter

                try:
                    url_photo = awsProvider.upload_file_s3(f'photo-perfil/{id_user}.jpg', photo_path)

                    await userRepository.create_user(user, url_photo)

                except Exception as e:
                    print(e)

                return {'message': 'Cadastro realizado com sucesso!'}

        except HTTPException as http_exception:
            raise http_exception
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Erro interno no servidor")
