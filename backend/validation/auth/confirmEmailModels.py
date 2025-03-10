from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

class RequestHeaderModel(BearerTokenTemplate):
    '''
        Request headers validator for /auth/ConfirmEmail
    '''
    
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
        examples=["AAABBB"],
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
