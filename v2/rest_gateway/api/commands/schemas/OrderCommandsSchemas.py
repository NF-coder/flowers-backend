from pydantic import BaseModel

class OrderSchema(BaseModel):
    orderId: int
    costumerFirstName: str
    costumerSecondName: str
    comment: str
    phoneNumber: str
    isFinished: bool
    isCanceled: bool
    country: str
    city: str
    street: str
    building: str
    flat: str
    userId: int
    productId: int
    orderStatus: str
    orderCreatedTimestamp: int