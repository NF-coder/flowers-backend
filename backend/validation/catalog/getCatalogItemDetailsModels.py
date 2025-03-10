from typing_extensions import Self, List, Annotated
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from ..components.CostDict import CostDict
from ..components.ReviewsDict import ReviewsDict

from libs.middleware.logic.schemas.CatalogSchemas import *

class RequestModel(BaseModel):
    '''
        Request validator for /catalog/getCatalogItemDetails
        Attributes:
            Authorization (str): user's Bearer token            
    '''
    id: int = Field(
        description="Catalog item id",
        example=1
    )

class ResponceSchema(BaseModel):
    title: str = Field(
        example="Букет из чего-то там"
    )
    author: str = Field(
        example="example@example.com",
    )
    titleImage: str = Field(
        example="http://example.com/example.png"
    )

    additionalImages: List[
        Annotated[
            str, Field(
            examples=["http://example.com/exampleAdditional.png"]
            )
        ]
    ]

    productId: int = Field(
        example=1
    )

    cost: CostDict
    reviews: ReviewsDict

    description: str = Field(
        example="Lorem Ipsum"
    )

    boughtTimesCounter: int = Field(
        default=100, # placeholder
        example=100
    )

    @staticmethod
    async def parse(CatalogObj: ProductDetailsSchema) -> Self:
        return ResponceSchema(
            title=CatalogObj.title,
            author=CatalogObj.supplierEmail,
            titleImage=CatalogObj.titleImage,
            additionalImages=CatalogObj.additionalImages,
            productId=CatalogObj.productId,
            cost=CostDict(
                costNum=CatalogObj.cost
            ),
            reviews=ReviewsDict(),
            description=CatalogObj.description
        )
