from pydantic import BaseModel

class GetProductsRequest(BaseModel):
    start: int
    count: int
    sort: str

class ProductIdModel(BaseModel):
    productId: int

class UserIdModel(BaseModel):
    userId: int

class GetMyProductsRequest(BaseModel):
    userId: int
    start: int
    count: int
    sort: str

class AddProductRequest(BaseModel):
    title: str
    titleImageUrl: str
    costNum: int
    description: str
    authorId: int