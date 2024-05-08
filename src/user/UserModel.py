from typing import List

from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    id: str
    name: str
    lastName: str
    email: EmailStr
    cep: str
    password: str
    position: str
    skills: List
    photo: str

    def __getitem__(self, item):
        return getattr(self, item)
