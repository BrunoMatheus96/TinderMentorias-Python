from fastapi import APIRouter

from src.auth.dto import Login
from src.auth.service import AuthService

router = APIRouter()


@router.post('/login')
async def login(dto: Login):
    service = AuthService()
    #Retorna o que foi feito no auth.service.py SE os dados enviados forem do tipo ao do auth.dto
    return service.login(dto)