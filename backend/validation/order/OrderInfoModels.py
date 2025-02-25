from typing_extensions import Self, List
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from ..components.GeoDict import GeoDict
from ..components.BeraerTokenTemplate import BearerTokenTemplate


class OrderInfoHeader(BearerTokenTemplate):
    pass

class OrderInfoQuery(BaseModel):
    orderId: int = Field(
        max_length=64
    )

class ResponceSchema(BearerTokenTemplate):
    orderId: str = Field(
        default="ok"
    )
    adress: GeoDict
    orderStatus: str
    orderCreatedTime: int
    customerPhone: str
    customerFirstName: str
    customerSecondName: str
    comment: str
    productIdArray: List[int]