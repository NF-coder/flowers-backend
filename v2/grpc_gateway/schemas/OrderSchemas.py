from typing_extensions import Self, Literal, List, Optional
from pydantic import BaseModel, Field

from ...database.fields.CatalogDB import CatalogDB

from datetime import datetime

from ...main.schemas.OrderSchemas import OrderDTO
from ...main.schemas.GeoSchemas import GeoDTO

class OrderSchema(BaseModel):
    orderId: int

    costumerFirstName: str
    costumerSecondName: Optional[str]
    comment: Optional[str]
    phoneNumber: Optional[str]

    isFinished: bool
    isCanceled: bool

    country: str
    city: str
    street: str
    building: int
    flat: str

    userId: int
    productId: int

    orderStatus: int
    orderCreatedTime: datetime

    @staticmethod
    async def parse(ProductObj: OrderDTO, GeoObj: GeoDTO) -> Self:
        return OrderSchema(
            orderId = ProductObj.userId,
            costumerFirstName = ProductObj.costumerFirstName,
            costumerSecondName = ProductObj.costumerSecondName,
            comment = ProductObj.comment,
            phoneNumber = ProductObj.comment,
            isFinished = ProductObj.isFinished,
            isCanceled = ProductObj.isCanceled,

            country = GeoObj.country,
            city = GeoObj.city,
            street = GeoObj.street,
            building = GeoObj.building,
            flat = GeoObj.flat,

            userId = ProductObj.userId,
            productId = ProductObj.productId,

            orderStatus = ProductObj.orderStatus,
            orderCreatedTime = ProductObj.orderCreatedTime
        )