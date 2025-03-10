from typing_extensions import Self, Literal, List
from pydantic import BaseModel, Field

from ...database.fields.CatalogDB import CatalogDB

class ProductDTO(BaseModel):
    productId: int
    supplierId: int
    title: str
    titleImage: str
    cost: int
    description: str

    @staticmethod
    async def parse(obj: CatalogDB) -> Self:
        return ProductDTO(
            productId=obj.id,
            supplierId=obj.supplierId,
            title=obj.title,
            titleImage=obj.titleImage,
            cost=obj.cost,
            description=obj.description
        )
    
class ProductDetailsDTO(ProductDTO):
    additionalImages: List[str]
