from typing_extensions import Self, List
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from ..components.GeoDict import GeoDict
from ..components.BeraerTokenTemplate import BearerTokenTemplate

class CancelOrderHeader(BearerTokenTemplate):
    pass

class CancelOrderBody(BaseModel):
    orderId: int

class ResponceSchema(BaseModel):
    status: str = Field(
        default="ok"
    )