from typing_extensions import Self, Literal, List, Dict
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate
from ..components.CostDict import CostDict

from exceptions import BasicException

class RequestHeaderModel(BearerTokenTemplate):
    '''
        Request headers validator for /supplier/addProduct
    '''

class RequestBodyModel(BaseModel):
    '''
        Request body validator for /supplier/addProduct
        Attributes:
            title (str): title of product card
            titleImage (str): user's id
            additionalImages (`list` of `str`): additional images URLs
            cost (dict): cost information wich contains
                - currency: str
                - costNum: int
            description (str): description of product
    '''
    title: str = Field(
        description="Title of product",
        examples="Букет из чего-то там",
        max_length=128
    )
    titleImage: str = Field(
        description="Url of main image",
        max_length=1024
    )
    additionalImages: List[str] = List[
        Field(
            description="Urls of additional images",
            max_length=1024
        )
    ]
    cost: CostDict
    description: str = Field(
        description="Description of product"
    )


class ResponceSchema(BaseModel):
    '''
        Responce schema item for /supplier/addProduct
        Attributes:
            status (str): product creation status
    '''
    status: str = Field(
        default="ok",
        description="Product creation status"
    )