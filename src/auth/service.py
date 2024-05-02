from fastapi import HTTPException

from src.auth.dto import Login


class AuthService:
    def login(self, dto: Login):
        if not (dto.login == 'admin@admin.com' and dto.password == 'teste123'):
            raise HTTPException(400, 'Login ou senha inválida')
        return {'message': 'Login realizado com sucesso'}
