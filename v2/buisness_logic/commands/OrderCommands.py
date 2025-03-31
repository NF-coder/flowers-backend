from .schemas.OrderModels import *

from simple_rpc import GrpcClient

class OrderCommands():
    def __init__(self, client: GrpcClient) -> None:
        self.find_unconfirmed_suppliers__ = client.configure_command(
            functionName="create_order",
            className="Order"
        )
        self.get_by_id__ = client.configure_command(
            functionName="get_by_id",
            className="Order"
        )
        self.get_active_by_userId__ = client.configure_command(
            functionName="get_active_by_userId",
            className="Order"
        )
        self.get_active_with_productId__ = client.configure_command(
            functionName="get_active_with_productId",
            className="Order"
        )
        self.set_status_by_id__ = client.configure_command(
            functionName="set_status_by_id",
            className="Order"
        )
        self.finish_by_id__ = client.configure_command(
            functionName="finish_by_id",
            className="Order"
        )
    
    async def create_order(
            self,
            geoId: int,
            userId: int,
            firstName: str,
            secondName: str,
            comment: str,
            phoneNumber: str,    
            productId: int
        ) -> OrderId:
        return OrderId.model_validate(
            await self.find_unconfirmed_suppliers__(
                geoId=geoId,
                userId=userId,
                firstName=firstName,
                secondName=secondName,
                comment=comment,
                phoneNumber=phoneNumber,
                productId=productId
            ),
            from_attributes=True
        )
    
    async def get_order_by_id(
            self,
            id: int
        ) -> OrderDTO:
        return OrderDTO.model_validate(
            await self.get_by_id__(
                id=id
            ),
            from_attributes=True
        )

    async def get_active_orders_by_userid(
            self,
            userId: int
        ) -> OrderDTOArray:
        return OrderDTOArray.model_validate(
            await self.get_active_by_userId__(
                userId=userId
            ),
            from_attributes=True
        )
    
    async def get_active_with_productId(
            self,
            productId: int
        ) -> OrderDTOArray:
        return OrderDTOArray.model_validate(
            await self.get_active_with_productId__(
                productId=productId
            ),
            from_attributes=True
        )
    
    async def set_status_by_id(
            self,
            orderId: int,
            newStatus: str
        ) -> None:
        await self.set_status_by_id__(
            id=orderId,
            newStatus=newStatus
        )
    
    async def finish_by_id(
            self,
            orderId: int
        ) -> None:
        await self.finish_by_id__(
            id=orderId
        )