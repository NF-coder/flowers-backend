from typing_extensions import Self, Literal, Dict
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

from ..components.CostDict import CostDict
from ..components.ReviewsDict import ReviewsDict

class RequestHeaderModel(BearerTokenTemplate):
    '''
        Request headers validator for /auth/myProductsList
    '''

class RequestQueryModel(BaseModel):
    '''
        Request query validator for /auth/myProductsList
        Attributes:
            start (int): index of first element
            count (int): number of elements
            sort (str): one of `time_upscending` `time_descending`. Other unimplemented
    '''
    start: int = 0,
    count: int = 20,
    sort: Literal["time_upscending", "time_descending"] = "time_descending"

class ResponceSchemaItem(BaseModel):
    title: str = Field(
        examples="Букет из чего-то там"
    )
    author: str = Field(
        examples="example@example.com",
    )
    image: str = Field(
        examples="http://example.com/example.png"
    )
    productId: int = Field(
        examples=1
    )

    cost: CostDict
    reviews: ReviewsDict
