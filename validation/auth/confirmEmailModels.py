from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

class RequestHeaderModel(BaseModel):
    '''
        Request headers validator for /auth/ConfirmEmail
        Attributes:
            Authorization (str): user's email
                - max-lenght - 128 chars
                - must correspond to the regex in AuthConfig.EMAIL_CHECKER_REGEX
            
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
    
class RequestBodyModel(BaseModel):
    '''
        Request body validator for /auth/ConfirmEmail
        Attributes:
            code (str): email confirmation code
                - max-lenght - 6 chars
                - must correspond to the regex in AuthConfig.EMAIL_CHECKER_REGEX
            
    '''
    code: str = Field(
        default=None,
        max_length=6,
        min_length=6,
        examples="AAABBB",
        description="Email confirmation code",
    )

class ResponceSchema(BaseModel):
    '''
        Responce schema for /api/{version}/auth/registerBasic
        Attributes:
            token (str): user's new jwt token
    '''
    token: str = Field(
        default="Bearer AAA.BBB.CCC",
        description="Bearer auth token"
    )
