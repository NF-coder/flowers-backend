from typing_extensions import Self, Literal
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

class RequestHeaderModel(BearerTokenTemplate):
    '''
        Request headers validator for /auth/listSuppliersRequests
    '''

class RequestQueryModel(BaseModel):
    '''
        Request query validator for /auth/listSuppliersRequests
        Attributes:
            start (int): index of first element
            count (int): number of elements
            sort (str): one of `time_upscending` `time_descending`
    '''
    start: int = 0,
    count: int = 20,
    sort: Literal["time_upscending", "time_descending"] = "time_descending"

class ResponceSchemaItem(BaseModel):
    '''
        Responce schema item for /api/{version}/auth/listSuppliersRequests
        Attributes:
            email (str): user's email
            id (int): user's id
    '''
    email: str = Field(
        examples="example@example.com",
        description="User's email"
    )
    id: int = Field(
        examples=1,
        description="User's id"
    )

