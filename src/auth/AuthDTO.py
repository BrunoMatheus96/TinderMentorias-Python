from pydantic import BaseModel, EmailStr, Field


class LoginDTO(BaseModel):
    login: EmailStr = Field(...)
    password: str = Field(...)
