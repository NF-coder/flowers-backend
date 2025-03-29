from typing_extensions import Self, List, Optional, Annotated
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
    SecondName: Optional[str] = Field(
        max_length=64
    )
    Comment: str = Field(
        max_length=1024
    )
    PhoneNumber: str = Field(
        max_length=32
    )


    ProductIdArray: Annotated[list[int], Field(examples=[1,2,3])]


class ResponceSchema(BaseModel):
    status: str = Field(
        default="ok"
    )
