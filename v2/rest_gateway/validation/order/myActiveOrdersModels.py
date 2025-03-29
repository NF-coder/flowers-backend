from typing_extensions import Self, List
from pydantic import BaseModel, Field, field_validator

from exceptions import BasicException

from ..components.GeoDict import GeoDict
from ..components.BeraerTokenTemplate import BearerTokenTemplate

from api.commands.schemas.OrderCommandsSchemas import *


class MyActiveOrdersHeader(BearerTokenTemplate):
    pass

class ResponceItemSchema(BaseModel):
    orderId: int
    adress: GeoDict
    orderStatus: str
    orderCreatedTime: int
    customerPhone: str
    customerFirstName: str
    customerSecondName: str
    comment: str
    productId: int

    @staticmethod
    async def parse(OrderObj: OrderSchema):
        return ResponceItemSchema(
            orderId=OrderObj.orderId,
            adress=GeoDict(
                Country=OrderObj.country,
                City=OrderObj.city,
                Street=OrderObj.street,
                Building=OrderObj.building,
                Flat=OrderObj.flat
            ),
            orderStatus=OrderObj.orderStatus,
            orderCreatedTime=OrderObj.orderCreatedTimestamp,
            costomerPhone=OrderObj.phoneNumber,
            customerFirstName=OrderObj.costumerFirstName,
            customerSecondName=OrderObj.costumerSecondName,
            comment=OrderObj.comment,
            productId=OrderObj.productId
        )