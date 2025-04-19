from typing_extensions import Self, Literal, List, Dict
from pydantic import BaseModel, Field, field_validator

from .BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException


class GeoDict(BaseModel):
    '''
        TODO: docstring
    '''
    Country: str = Field(
        max_length=128,
        example="Russia"
    )
    City: str = Field(
        max_length=128,
        example="St. Petersburg"
    )
    Street: str = Field(
        max_length=128,
        example="Lensiveta"
    )
    Building: str = Field(
        max_length=128,
        example="23А"
    )
    Flat: str = Field(
        max_length=128,
        example="198"
    )
    
