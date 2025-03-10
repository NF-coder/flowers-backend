from ..main.Order import Order

from ..main.Geo import Geo

from .schemas.OrderSchemas import *

from typing_extensions import List, Self, Optional
from exceptions import BasicException

Order = Order()
Geo = Geo()

class OrderLogic():
    @staticmethod
    def __init__(self) -> Self:
        pass
    
    async def create_order(
            country: str,
            city: str,
            street: str,
            building: str,
            flat: str,
            userId: int,

            productIdArray: List[int],
            firstName: str,
            phoneNumber: str,

            secondName: Optional[str] = None,
            comment: Optional[str] = None
        ) -> None:
        geoId = await Geo.add_geo(
            country=country,
            city=city,
            street=street,
            building=building,
            flat=flat,
            userId=userId
        )

        for productId in productIdArray:
            await Order.create_order(
                geoId=geoId,
                userId=userId,
                firstName=firstName,
                secondName=secondName,
                comment=comment,
                phoneNumber=phoneNumber,
                productId=productId
            )
    
    async def order_info(
            orderId: int
        ) -> OrderSchema:
        order = await Order.get_by_id(
            id=orderId
        )
        geo = await Geo.get_by_id(
            id=order.geoId
        )
        return await OrderSchema.parse(order, geo)
    
    async def get_active_by_userId(
            userId: int
        ) -> List[OrderSchema]:
        orders = await Order.get_active_by_userId(
            userId=userId
        )
        out = []
        for order in orders:
            geo = await Geo.get_by_id(
                id=order.geoId
            )
            out.append(
                await OrderSchema.parse(order, geo)
            )
        return out