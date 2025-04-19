from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException


class BearerTokenTemplate(BaseModel):
    '''
        Bearer token validator
        Attributes:
            HTTPBearer (str): Bearer token
    '''
    HTTPBearer: str = Field(
        default=None,
        example="Bearer AAA.BBB.CCC",
        description="Bearer auth token",
    )

    @field_validator('HTTPBearer', mode='after')
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