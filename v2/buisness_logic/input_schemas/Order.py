from pydantic import BaseModel

class CreateOrderReq(BaseModel):
    country: str
    city: str
    street: str
    building: str
    flat: str
    userId: int
    
    productIdArray: list[int]
    firstName: str
    phoneNumber: str
    
    secondName: str
    comment: str

class OredrIdReq(BaseModel):
    orderId: int

class UserIdReq(BaseModel):
    userId: int