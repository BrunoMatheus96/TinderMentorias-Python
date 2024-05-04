from typing import List

from pydantic import BaseModel, EmailStr, Field


class RegisterDTO(BaseModel):
    name: str = Field(..., min_length=2)
    lastName: str = Field(..., min_length=3)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    password: str
    position: str
    skills: List
    photo: str = 'Arquivo (pnj, jpg, etc)'
