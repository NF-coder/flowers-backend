from typing_extensions import Self, Literal, List, Dict
from pydantic import BaseModel, Field, field_validator

from .BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException


class ReviewsDict(BaseModel):
    '''
        TODO: docstring
    '''
    rank: float = Field(
        description="Item rank",
        default=4.0,
        examples=5.0,
        ge=0,
        le=5
    )
    reviewsCount: int = Field(
        examples=0,
        default=10, # микронаёбка)
        description="Number of reviews"
    )
