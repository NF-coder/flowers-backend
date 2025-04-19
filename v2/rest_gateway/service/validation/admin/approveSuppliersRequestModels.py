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
            id (int): user's id
    '''
    id: int = Field(
        default=None,
        description="User id"
    )

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