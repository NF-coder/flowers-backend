from typing_extensions import Self, Literal
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

class RequestHeaderModel(BearerTokenTemplate):
    '''
        Request headers validator for /auth/listSuppliersRequests
    '''

class RequestBodyModel(BaseModel):
    '''
        Request body validator for /auth/listSuppliersRequests
        Attributes:
            email (str): user's email
            id (int): user's id
        ## WARNING!
            It doesn't check if one of email/id specified
    '''
    email: str = Field(
        default=None,
        description="User's email"
    ),
    id: int = Field(
        default=None,
        description="User's id"
    ),

class ResponceSchema(BaseModel):
    '''
        Responce schema item for /api/{version}/auth/approveSuppliersRequest
        Attributes:
            status (str): supplier confirmation status
    '''
    status: str = Field(
        default="ok",
        description="Confirmation status"
    )