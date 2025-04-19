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
    userId: int = Field(
        example=1,
        description="User's id"
    )
    type: str = Field(
        example="supplier",
        description="Account type"
    )
    isConfirmed: bool = Field(
        example=False,
        description="Unused field?"
    )
    isSupplierStatusConfirmed: bool = Field(
        example=True,
        description="Is supplier status confirmed by admin"
    )
    isAdmin: bool = Field(
        example=True,
        description="Is user admin"
    )
