from pydantic import BaseModel

class OrderId(BaseModel):
    id: int

class ProductId(BaseModel):
    productId: int

class OrderDTO(BaseModel):
    orderId: int

    costumerFirstName: str
    costumerSecondName: str
    comment: str
    phoneNumber: str

    isFinished: bool
    isCanceled: bool

    geoId: int
    userId: int
    productId: int

    orderStatus: str
    orderCreatedTime: int

class OrderDTOArray(BaseModel):
    OrderDTOArray: list[OrderDTO]