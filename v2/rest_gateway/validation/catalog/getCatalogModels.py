from typing_extensions import Self, Literal, Dict
from pydantic import BaseModel, Field, field_validator

from ..components.BeraerTokenTemplate import BearerTokenTemplate

from exceptions import BasicException

from ..components.CostDict import CostDict
from ..components.ReviewsDict import ReviewsDict

from api.commands.schemas.CatalogCommandsSchemas import *

class RequestQueryModel(BaseModel):
    start: int = 0,
    count: int = 20,
    sort: Literal["time_upscending", "time_descending"] = "time_descending"
    category: str # not used

class ResponceSchemaItem(BaseModel):
    title: str = Field(
        example="Букет из чего-то там"
    )
    author: int = Field(
        example=1,
    )
    image: str = Field(
        example="http://example.com/example.png"
    )
    productId: int = Field(
        example=1
    )

    cost: CostDict
    reviews: ReviewsDict

    @staticmethod
    async def parse(CatalogObj: ProductSchema) -> Self:
        return ResponceSchemaItem(
            title=CatalogObj.title,
            author=CatalogObj.supplierId,
            image=CatalogObj.titleImage,
            productId=CatalogObj.productId,
            cost=CostDict(
                costNum=CatalogObj.cost
            ),
            reviews=ReviewsDict()
        )
