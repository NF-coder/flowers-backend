from typing_extensions import Self, Literal
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

from libs.middleware.logic.schemas.AdminSchemas import *

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
    start: int = Field(
        example=0,
        default=0,
        description="First element index"
    )
    count: int = Field(
        example=20,
        default=20,
        description="Count of elements in result array (can be less than specified)"
    )
    sort: Literal["time_upscending", "time_descending"] = "time_descending"

class ResponceSchemaItem(BaseModel):
    '''
        Responce schema item for /api/{version}/auth/listSuppliersRequests
        Attributes:
            email (str): user's email
            id (int): user's id
    '''
    email: str = Field(
        example="example@example.com",
        description="User email"
    )
    id: int = Field(
        example=1,
        description="User id"
    )

    @staticmethod
    async def parse(UserObj: UserSchema) -> Self:
        return ResponceSchemaItem(
            email=UserObj.email,
            id=UserObj.userId
        )
