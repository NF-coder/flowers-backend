from typing_extensions import Self, List
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from ..components.GeoDict import GeoDict
from ..components.BeraerTokenTemplate import BearerTokenTemplate


class CreateOrderHeaderModel(BearerTokenTemplate):
    pass

class CreateOrderBody(BaseModel):
    Geo: GeoDict

    FirstName: str = Field(
        max_length=64
    )
    SecondName: str = Field(
        max_length=64
    )
    Comment: str = Field(
        max_length=1024
    )
    PhoneNumber: str = Field(
        max_length=32
    )


    ProductIdArray: List[int] = List[Field(examples=[1,2,3])]

class ResponceSchema(BearerTokenTemplate):
    status: str = Field(
        default="ok"
    )
