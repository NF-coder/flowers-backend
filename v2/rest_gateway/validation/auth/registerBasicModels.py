from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from settings import AuthConfig

class RequestModel(BaseModel):
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
        description="User email",
        example="example@example.com"
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
    def check_account_type(cls: Self, type: str) -> str:
        '''
            Checks if account type exists in AuthConfig.AVAILABLE_ACCOUNT_TYPES
            Raises:
                BasicException:
                    - code: `400`
                    - description: `Unprocassable type of account`
        '''
        if type not in AuthConfig.AVAILABLE_ACCOUNT_TYPES:
            raise BasicException(400, 'Unprocassable type of account')
        return type

class ResponceSchema(BaseModel):
    '''
        Responce schema for /api/{version}/auth/registerBasic
        Attributes:
            token (str): user's jwt token
    '''
    token: str = Field(default="Bearer AAA.BBB.CCC")