from typing_extensions import Self, Literal, List, Dict
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException


class CostDict(BaseModel):
    '''
        TODO: docstring
    '''
    currency: str = Field(
        description="Currency of cost",
        examples="RUB",
        max_length=128
    ) # и потом я крутейше отброшу это поле)
    costNum: int = Field(
        description="Cost of product"
    )
