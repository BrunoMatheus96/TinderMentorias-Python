from typing import List

from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    name: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    cep: str = Field(...)
    password: str = Field(...)
    position: str = Field(...)
    skills: List = Field(...)
    photo: str = Field(...)


class NewUserModel(BaseModel):
    name: str = Field(...)
    lastName: str = Field(...)
    email: EmailStr = Field(...)
    cep: str = Field(...)
    password: str = Field(...)
    position: str = Field(...)
    skills: List = Field(...)
    photo: str = Field(...)


class UserLoginModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
