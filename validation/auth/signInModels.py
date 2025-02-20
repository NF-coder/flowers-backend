from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

class RequestModel(BaseModel):
    '''
        Request validator for /auth/signIn
        Attributes:
            Authorization (str): user's Bearer token            
    '''
    Authorization: str = Field(
        default=None,
        examples="Basic base64(user:password)",
        description="Basic auth token",
    )

    @field_validator('Authorization', mode='after')
    @classmethod
    def check_basic_auth_token(cls: Self, token: str) -> str:
        '''
            Check if Basic token has valid format
            Raises:
                BasicException:
                    - code: `400`
                    - description: `Invalid form of Basic Authentification token`
        '''
        if token[:6] != "Basic ":
            raise BasicException(400, 'Invalid form of Basic Authentification token')
        return token

class ResponceSchema(BaseModel):
    '''
        Responce schema for /api/{version}/auth/registerBasic
        Attributes:
            token (str): user's jwt token
    '''
    token: str = Field(default="Bearer AAA.BBB.CCC")