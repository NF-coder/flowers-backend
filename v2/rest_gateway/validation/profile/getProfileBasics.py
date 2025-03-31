from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

class RequestModel(BearerTokenTemplate):
    '''
        Request headers validator for /auth/ConfirmEmail
    '''

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
