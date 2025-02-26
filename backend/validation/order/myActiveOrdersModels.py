from typing_extensions import Self, List
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from ..components.GeoDict import GeoDict
from ..components.BeraerTokenTemplate import BearerTokenTemplate


class MyActiveOrdersHeader(BearerTokenTemplate):
    pass

class ResponceItemSchema(BaseModel):
    orderId: int
    adress: GeoDict
    orderStatus: str
    orderCreatedTime: int
    customerPhone: str
    customerFirstName: str
    customerSecondName: str
    comment: str
    productIdArray: List[int]