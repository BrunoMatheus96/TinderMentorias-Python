import re
from typing import List

from fastapi import UploadFile
from pydantic import BaseModel, EmailStr, Field, validator


class RegisterDTO(BaseModel):
    name: str = Field(..., min_length=2)
    lastName: str = Field(..., min_length=3)
    email: EmailStr
    cep: str = Field(..., min_length=8, max_length=8)
    password: str = Field(..., min_length=6)
    position: str = Field(..., min_length=1)
    skills: List = Field(..., max_items=5)
    photo: UploadFile