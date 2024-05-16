import os
from datetime import datetime

from fastapi import HTTPException

from src.core.util.ResponseDTO import ResponseDTO
from src.user.UserDTO import RegisterDTO, UpdateUserDTO
from src.user.UserRepository import UserRepository
from src.auth.providers.AWSProvider import AWSProvider

userRepository = UserRepository()

awsProvider = AWSProvider()


class UserService:
    async def user_register(self, user: RegisterDTO, photo_path):

        # Validações da senha DTO
        special_characters = "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~"
        has_special_char = any(char in special_characters for char in user.password)
        has_digit = any(char.isdigit() for char in user.password)
        if not has_special_char or not has_digit:
            raise HTTPException(400, "A senha deve conter letra, número e caracter especial")

        try:
            user_found = await userRepository.search_for_user_by_email(user.email)

            if user_found:
                print(user_found)
                os.remove(photo_path)
                raise HTTPException(400, f'O email {user.email} já está cadastrado no sistema')
            else:

                try:
                    url_photo = awsProvider.upload_file_s3(
                        f'photo-perfil/{datetime.now().strftime("%d%m%y%H%M%S")}.jpg', photo_path)

                    await userRepository.create_user(user, url_photo)

                except Exception as e:
                    print(e)

                return {'detail': 'Cadastro realizado com sucesso!'}

        except HTTPException as http_exception:
            raise http_exception
        except Exception as e:
            print(e)
            raise HTTPException(500, "Erro interno no servidor")

    async def find_user(self, id: str):
        finded_user = await userRepository.search_for_user_by_id(id)

        return ResponseDTO('Usuário encontrado', finded_user, 200)

    async def update_user(self, id, update_user: UpdateUserDTO, photo_path):

        # Validações da senha DTO
        special_characters = "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~"
        has_special_char = any(char in special_characters for char in update_user.password)
        has_digit = any(char.isdigit() for char in update_user.password)
        if not has_special_char or not has_digit:
            raise HTTPException(400, "A senha deve conter letra, número e caracter especial")

        try:
            find_user = await userRepository.search_for_user_by_id(id)

            if find_user:
                user_dict = update_user.__dict__

                try:
                    photo = find_user.photo[61:]
                    awsProvider.delete_file_S3(photo)

                    url_photo = awsProvider.upload_file_s3(
                        f'photo-perfil/{datetime.now().strftime("%d%m%y%H%M%S")}.jpg', photo_path)

                    user_dict['photo'] = url_photo

                    #await userRepository.update_user(id, {'photo': url_photo})

                    updated_user = await userRepository.update_user(id, user_dict)

                    return ResponseDTO('Dados atualizados com sucesso', updated_user, 200)

                except Exception as e:
                    print(e)
                    raise HTTPException(500, "Erro interno no servidor")

        except Exception as e:
            print(e)
            raise HTTPException(500, "Erro interno no servidor")
