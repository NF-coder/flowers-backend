from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

class RequestModel(BaseModel):
    '''
        Request headers validator for /auth/ConfirmEmail
        Attributes:
            Authorization (str): Bearer token
            
    '''
    Authorization: str = Field(
        default=None,
        examples="Bearer AAA.BBB.CCC",
        description="Bearer auth token",
    )

    @field_validator('Authorization', mode='after')
    @classmethod
    def check_basic_auth_token(cls: Self, token: str) -> str:
        '''
            Check if Basic token has valid format
            Raises:
                BasicException:
                    - code: `400`
                    - description: `Invalid form of Bearer Authentification token`
        '''      
        if token[:7] != "Bearer ":
            raise BasicException(400, 'Invalid form of Bearer Authentification token')
        return token

class ResponceSchema(BaseModel):
    '''
        Responce schema for /api/{version}/auth/registerBasic
        Attributes:
            status (str): user deletion operation status
    '''
    status: str = Field(
        default="ok",
        description="Deletion status"
    )
