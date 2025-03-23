from typing_extensions import Self, Literal, List
from pydantic import BaseModel, Field

from ...main.schemas.CatalogSchemas import ProductDTO
from ...main.schemas.UsersSchemas import UserDTO

class ProductSchema(BaseModel):
    productId: int
    supplierId: int
    supplierEmail: str
    title: str
    titleImage: str
    cost: int
    description: str

    @staticmethod
    async def parse(UserObj: UserDTO, ProductObj: ProductDTO) -> Self:
        return ProductSchema(
            productId=ProductObj.productId,
            supplierId=UserObj.userId,
            supplierEmail=UserObj.email,
            title=ProductObj.title,
            titleImage=ProductObj.titleImage,
            cost=ProductObj.cost,
            description=ProductObj.description
        )
    
class ProductDetailsSchema(ProductSchema):
    additionalImages: List[str]

    @staticmethod
    async def parse(UserObj: UserDTO, ProductObj: ProductDTO, AdditionalImagesArr: List[str]) -> Self:
        return ProductDetailsSchema(
            productId=ProductObj.productId,
            supplierId=UserObj.userId,
            supplierEmail=UserObj.email,
            title=ProductObj.title,
            titleImage=ProductObj.titleImage,
            cost=ProductObj.cost,
            description=ProductObj.description,
            additionalImages=AdditionalImagesArr
        )