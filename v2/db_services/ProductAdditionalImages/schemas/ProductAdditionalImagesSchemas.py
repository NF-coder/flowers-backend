from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

from database.ProductAdditionalImagesDB import ProductAdditionalImagesDB

class AdditionalImagesDTO(BaseModel):
    id: int
    imageUrl: str
    productId: int

    @staticmethod
    async def parse(obj: ProductAdditionalImagesDB) -> Self:
        return AdditionalImagesDTO(
            id=obj.id,
            productId=obj.productId,
            imageUrl=obj.imageUrl
        )

class AdditionalImagesDTOArray(BaseModel):
    AdditionalImagesDTOArray: list[AdditionalImagesDTO]