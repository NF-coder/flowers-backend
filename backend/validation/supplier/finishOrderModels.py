from typing_extensions import Self, Literal, Dict
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

from ..components.CostDict import CostDict
from ..components.ReviewsDict import ReviewsDict

class RequestHeaderModel(BearerTokenTemplate):
    pass

class RequestQueryModel(BaseModel):
    orderId: int = 0

class ResponceSchema(BaseModel):
    status: str = Field(
        default="ok",
        description="Product creation status"
    )
