from ...libs.middleware.logic.schemas.OrderSchemas import *
from ...validation.components.GeoDict import GeoDict

class orderSerializers:
    @staticmethod
    def __init__(self): pass

    async def orderInfoSerializer(
            data: OrderSchema,
            ResponceModel,
            GeoDictModel: GeoDict
        ):
        return ResponceModel(
            orderId=data.orderId,
            adress=GeoDict(
                Country=data.country,
                City=data.city,
                Street=data.street,
                Building=data.building,
                Flat=data.flat
            ),
            orderStatus=data.orderStatus,
            orderCreatedTime=int(data.orderCreatedTime.timestamp()),
            customerPhone=data.phoneNumber,
            customerFirstName=data.costumerFirstName,
            customerSecondName=data.costumerFirstName,
            comment=data.comment,
            product=data.productId
        )