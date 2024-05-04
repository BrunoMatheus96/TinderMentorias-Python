import os
from datetime import datetime
from fastapi import HTTPException
from src.user.UserDTO import RegisterDTO
from src.user.UserModel import NewUserModel
from src.user.UserRepository import UserRepository
from src.auth.providers.AWSProvider import AWSProvider

userRepository = UserRepository()
awsProvider = AWSProvider()


class UserService:
    async def user_register(self, dto: RegisterDTO):

        user = NewUserModel(
            name=dto.name,
            lastName=dto.lastName,
            email=dto.email,
            cep=dto.cep,
            password=dto.password,
            position=dto.position,
            skills=dto.skills,
            photo=dto.photo
        )

        # Validações do DTO
        special_characters = "!@#$%^&*()-_+=<>,.?/:;{}[]|\\~"
        has_special_char = any(char in special_characters for char in dto.password)
        has_digit = any(char.isdigit() for char in dto.password)
        if not has_special_char or not has_digit:
            raise HTTPException(status_code=400,
                                detail="A senha deve conter letra, número e caracter especial")

        try:
            user_found = await userRepository.search_for_user_by_email(user.email)

            if user_found:
                print(user_found)
                raise HTTPException(status_code=400, detail=f'O email {user.email} já está cadastrado no sistema')
            else:
                if dto.photo:
                    try:
                        file_name = f'photo-{datetime.now().strftime("%H%M%S")}.jpg'
                        file_path = f'files/{file_name}'

                        with open(file_path, 'wb+') as file:
                            file.write(dto.photo.file.read())

                        url_photo = awsProvider.upload_file_s3(file_name, file_path)
                        os.remove(file_path)

                        user.photo = url_photo
                    except Exception as e:
                        print(f"Erro ao fazer upload da foto: {e}")

                await userRepository.create_user(user)

                return {'message': 'Cadastro realizado com sucesso!'}

        except HTTPException as http_exception:
            raise http_exception
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Erro interno no servidor")
