from typing_extensions import Self, Literal, List, Dict
from pydantic import BaseModel, Field, field_validator

from .BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException


class GeoDict(BaseModel):
    '''
        TODO: docstring
    '''
    Country: str = Field(
        max_length=128
    )
    City: str = Field(
        max_length=128
    )
    Street: str = Field(
        max_length=128
    )
    Building: str = Field(
        max_length=128
    )
    Flat: str = Field(
        max_length=128
    )
    
