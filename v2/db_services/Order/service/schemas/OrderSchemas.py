from typing_extensions import Self, Literal, List, Optional
from pydantic import BaseModel, Field

from datetime import datetime

from database.OrderDB import OrderDB

class OrderDTO(BaseModel):
    orderId: int

    costumerFirstName: str
    costumerSecondName: Optional[str]
    comment: Optional[str]
    phoneNumber: Optional[str]

    isFinished: bool
    isCanceled: bool

    geoId: int
    userId: int
    productId: int

    orderStatus: str
    orderCreatedTime: int

    @staticmethod
    async def parse(obj: OrderDB) -> Self:
        return OrderDTO(
            orderId=obj.id,
            costumerFirstName=obj.costumerFirstName,
            costumerSecondName=obj.costumerSecondName,
            comment=obj.comment,
            phoneNumber=obj.phoneNumber,
            isFinished=obj.isFinished,
            isCanceled=obj.isCanceled,
            geoId=obj.geoId,
            userId=obj.userId,
            productId=obj.productId,
            orderStatus=obj.orderStatus,
            orderCreatedTime=obj.orderCreatedTime.timestamp()//1
        )

class OrderDTOArray(BaseModel):
    OrderDTOArray: List[OrderDTO]