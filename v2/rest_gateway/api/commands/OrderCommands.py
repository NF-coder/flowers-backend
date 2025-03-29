from .schemas.OrderCommandsSchemas import *

from simple_rpc import GrpcClient

class OrderCommands:
    def __init__(self, client: GrpcClient) -> None:
        self.create_order__ = client.configure_command(
            functionName="create_order",
            className="OrderLogic"
        )
        self.order_info__ = client.configure_command(
            functionName="order_info",
            className="OrderLogic"
        )
        self.get_active_by_userId__ = client.configure_command(
            functionName="get_active_by_userId",
            className="OrderLogic"
        )
    
    async def create_order(
            self,
            country: str,
            city: str,
            street: str,
            building: str,
            flat: str,
            userId: int,
            productIdArray: list[int],
            firstName: str,
            phoneNumber: str,
            secondName: str,
            comment: str
        ) -> None:
        await self.create_order__(
            country=country,
            city=city,
            street=street,
            building=building,
            flat=flat,
            userId=userId,
            productIdArray=productIdArray,
            firstName=firstName,
            phoneNumber=phoneNumber,
            secondName=secondName,
            comment=comment
        )
    
    async def order_info(self, orderId: int) -> OrderSchema:
        responce =  await self.order_info__(
            orderId=orderId
        )
        return OrderSchema.model_validate(
            responce,
            from_attributes=True
        )

    async def get_active_by_userId(self, userId: int) -> list[OrderSchema]:
        responce =  await self.get_active_by_userId__(
            userId = userId
        )
        return [
            OrderSchema.model_validate(
                order,
                from_attributes=True
            )
            for order in responce.OrderSchemasArray
        ]