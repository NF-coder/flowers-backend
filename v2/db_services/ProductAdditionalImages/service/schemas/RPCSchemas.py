from pydantic import BaseModel

class EmptyModel(BaseModel):
    pass

class AddImagesRequest(BaseModel):
    imageUrls: list[str]
    productId: int

class ProductIdModel(BaseModel):
    productId: int