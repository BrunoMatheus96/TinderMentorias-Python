from fastapi import Header, HTTPException

from src.auth.AuthService import AuthService

authService = AuthService()


async def check_token(authorization: str = Header(default='')):
    if not authorization.split(' ')[0] == 'Bearer':
        raise HTTPException(status_code=401, detail="Necessário token para autenticação.")

    token = authorization.split(' ')[1]

    payload = authService.decode_token_jwt(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado.")

    return payload
