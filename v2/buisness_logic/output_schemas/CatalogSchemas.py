from typing_extensions import Self, Literal, List
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    productId: int
    supplierId: int
    title: str
    titleImage: str
    cost: int
    description: str

    @staticmethod
    async def parse(ProductObj) -> Self:
        print(ProductObj)
        return ProductSchema(
            productId=ProductObj.productId,
            supplierId=ProductObj.supplierId,
            title=ProductObj.title,
            titleImage=ProductObj.titleImage,
            cost=ProductObj.cost,
            description=ProductObj.description
        )
    
class ProductDetailsSchema(ProductSchema):
    additionalImages: List[str]

    @staticmethod
    async def parse(ProductObj, AdditionalImagesArr: List[str]) -> Self:
        return ProductDetailsSchema(
            productId=ProductObj.productId,
            supplierId=ProductObj.supplierId,
            title=ProductObj.title,
            titleImage=ProductObj.titleImage,
            cost=ProductObj.cost,
            description=ProductObj.description,
            additionalImages=AdditionalImagesArr
        )

class ProductSchemasArray(BaseModel):
    ProductSchemasArray: list[ProductSchema]