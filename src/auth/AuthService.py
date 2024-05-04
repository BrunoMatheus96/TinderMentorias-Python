from fastapi import HTTPException

from src.auth.AuthDTO import LoginDTO


class AuthService:
    def login(self, dto: LoginDTO):
        if not (dto.login == 'admin@admin.com' and dto.password == 'teste123'):
            raise HTTPException(400, 'Login ou senha inválida')
        return {'message': 'Login realizado com sucesso'}
