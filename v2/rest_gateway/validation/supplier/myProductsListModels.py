from typing_extensions import Self, Literal, Dict
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

from ..components.CostDict import CostDict
from ..components.ReviewsDict import ReviewsDict
from libs.middleware.logic.schemas.SupplierSchemas import ProductSchema

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

class ResponceItemSchema(BaseModel):
    title: str = Field(
        example="Букет из чего-то там"
    )
    author: str = Field(
        example="example@example.com",
    )
    image: str = Field(
        example="http://example.com/example.png"
    )
    productId: int = Field(
        examples=[1]
    )

    cost: CostDict
    reviews: ReviewsDict

    async def parse(ProductObj: ProductSchema) -> Self:
        return ResponceItemSchema(
            title=ProductObj.title,
            author=ProductObj.supplierEmail,
            image=ProductObj.titleImage,
            productId=ProductObj.productId,

            cost=CostDict(
                costNum=ProductObj.cost
            ),
            reviews=ReviewsDict()
        )