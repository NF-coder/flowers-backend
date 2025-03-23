from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

class CreateOrderReq(BaseModel):
    geoId: int
    userId: int
    productId: int
    firstName: str
    secondName: str
    comment: str
    phoneNumber: str

class OrderIdModel(BaseModel):
    id: int

class ProductIdModel(BaseModel):
    productId: int

class EmptyModel(BaseModel):
    pass

class SetStatusByIdRequest(BaseModel):
    id: int
    newStatus: str