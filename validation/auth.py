import re

from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator, field_validator

from exceptions import BasicException

from settings import AuthConfig

class SignIn(BaseModel):
    '''
        Request validator for /auth/signIn
        Attributes:
            Authorization (str): user's email
                - max-lenght - 128 chars
                - must correspond to the regex in AuthConfig.EMAIL_CHECKER_REGEX
            
    '''
    Authorization: str = Field(
        default=None,
        examples="Basic base64(user:password)",
        description="Bearer auth token",
    )

    @field_validator('Authorization', mode='after')
    @classmethod
    def check_basic_auth_token(cls, token: str) -> str:
        '''
            Check if Basic token has valid format
        '''
        if token[:6] != "Basic ":
            raise BasicException('Invalid form of Basic Authentification token')
        return token

class RegisterBasic(BaseModel):
    '''
        Request validator for /auth/registerBasic
        Attributes:
            email (str): user's email
                - max-lenght - 128 chars
                - must correspond to the regex in AuthConfig.EMAIL_CHECKER_REGEX
            password (str):  user's password
                - min_lenght - 8 chars
                - max_lenght - 64 chars
            type (str): user's account type
                - must be one from list in AuthConfig.AVAILABLE_ACCOUNT_TYPES
    '''
    email: str = Field(
        max_length=128,
        pattern=AuthConfig.EMAIL_CHECKER_REGEX,
        frozen=True,
        description="User email"
    )
    password: str = Field(
        min_length=8,
        max_length=64,
        frozen=True,
        description="User password"
    )
    type: str = Field(frozen=True, description="Account type")
    
    @field_validator("type", mode="after")
    @classmethod
    def check_account_type(cls, type: str) -> str:
        '''
            Checks if account type exists in AuthConfig.AVAILABLE_ACCOUNT_TYPES
            Parameters:
                type (str): user's account type
            Returns:
                type (str): user's account type
        '''
        if type not in AuthConfig.AVAILABLE_ACCOUNT_TYPES:
            raise BasicException(400, 'Неизвестный тип аккаунта')
        return type

class RespSchemaRegisterBasic(BaseModel):
    '''
        Response schema for /api/{version}/auth/registerBasic
        Attributes:
            token (str): user's jwt token
    '''
    token: str = Field(default="Bearer AAA.BBB.CCC")