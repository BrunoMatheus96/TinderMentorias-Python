from pydantic import BaseModel, EmailStr, Field


class LoginDTO(BaseModel):
    login: EmailStr = Field(..., description="O e-mail usado para fazer login")
    password: str = Field(..., description="A senha do usuário")
