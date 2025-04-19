from pydantic import BaseModel

class ProductId(BaseModel):
    productId: int

class AdditionalImagesDTO(BaseModel):
    id: int
    imageUrl: str
    productId: int

class AdditionalImagesDTOArray(BaseModel):
    AdditionalImagesDTOArray: list[AdditionalImagesDTO]