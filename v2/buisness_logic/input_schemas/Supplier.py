from pydantic import BaseModel

class AddProductReq(BaseModel):
    title: str
    titleImageUrl: str
    costNum: int
    description: str
    authorId: int
    additionalImagesUrls: list[str]

class MyProductsListReq(BaseModel):
    userId: int
    start: int
    count: int
    sort: str

class UserIdReq(BaseModel):
    userId: int

class SetOrderStatusReq(BaseModel):
    orderId: int
    newStatus: str

class OrderIdReq(BaseModel):
    orderId: int