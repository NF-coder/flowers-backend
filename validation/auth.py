import re

from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator, field_validator

class SignIn(BaseModel):
    Authorization: str = Field(default=None, description="Bearer auth token")

    @field_validator('Authorization', mode='after')
    @classmethod
    def check_basic_auth_token(self) -> Self:
        '''
            Check if Basic token has valid format
        '''
        if self.Authorization[:6] != "Basic ":
            raise ValueError('Invalid form of Basic Authentification token')
        return self

class RegisterBasic(BaseModel):
    email: str = Field(default=None, description="User email")
    password: str = Field(default=None, description="User passwoed")
    type: str = Field(default=None, description="Account type email")

    @field_validator("email", mode="after")
    @classmethod
    def check_email(self) -> Self:
        if not re.match(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values