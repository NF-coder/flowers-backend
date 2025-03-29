from pydantic import BaseModel

class ProductSchema(BaseModel):
    productId: int
    supplierId: int
    title: str
    titleImage: str
    cost: int
    description: str