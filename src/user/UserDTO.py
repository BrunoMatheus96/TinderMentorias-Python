from typing import List, Optional

from fastapi import HTTPException, UploadFile
from pydantic import BaseModel, EmailStr, Field, field_validator

from src.core.util.DecoratorUtil import DecoratorUtil

decoratorUtil = DecoratorUtil()


@decoratorUtil.form_body
class RegisterDTO(BaseModel):
    name: str = Field(..., min_length=2)
    lastName: str = Field(..., min_length=3)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    password: str = Field(..., min_length=6, max_length=20)
    position: str = Field(..., min_length=1)
    skills: List = Field(..., max_items=5)
    interests: List = Field(..., max_items=5)


@decoratorUtil.form_body
class UpdateUserDTO(BaseModel):
    name: str
    lastName: str = Field(..., min_length=3)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    password: str = Field(..., min_length=6)
    position: str = Field(..., min_length=1)
    skills: List = Field(..., max_items=5)
    interests: List = Field(..., max_items=5)
    photo: UploadFile = Field(...)

    @field_validator('name')
    @classmethod
    def validate_name_length(cls, value):
        if len(value) < 2:
            raise HTTPException(400, 'O nome deve possuir no mínimo 2 caracteres')
        return value
