from .schemas.SupplierCommandsSchemas import *

from simple_rpc import GrpcClient

class SupplierCommands:
    def __init__(self, client: GrpcClient) -> None:
        self.add_product__ = client.configure_command(
            functionName="add_product",
            className="SupplierLogic"
        )
        self.my_products_list__ = client.configure_command(
            functionName="my_products_list",
            className="SupplierLogic"
        )
        self.orders_for_me__ = client.configure_command(
            functionName="orders_for_me",
            className="SupplierLogic"
        )
        self.set_status__ = client.configure_command(
            functionName="set_status",
            className="SupplierLogic"
        )
        self.finish_order__ = client.configure_command(
            functionName="finish_order",
            className="SupplierLogic"
        )


    async def add_product(
        self,
        title: str,
        titleImageUrl: str,
        costNum: int,
        description: str,
        authorId: int,
        additionalImagesUrls: list[str]
    ) -> None:
        await self.add_product__(
            title=title,
            titleImageUrl=titleImageUrl,
            costNum=costNum,
            description=description,
            authorId=authorId,
            additionalImagesUrls=additionalImagesUrls
        )
    
    async def my_products_list(
        self,
        userId: int,
        start: int,
        count: int,
        sort: str
    ) -> list[ProductSchema]:

        responce =  await self.my_products_list__(
            userId=userId,
            start=start,
            count=count,
            sort=sort
        )
        
        return [
            ProductSchema.model_validate(
                obj,
                from_attributes=True
            )
            for obj in responce.ProductSchemasArray
        ]
    
    async def orders_for_me(self, userId: int) -> list[OrderSchema]:
        responce =  await self.orders_for_me__(
            userId=userId
        )
        
        return [
            OrderSchema.model_validate(
                obj,
                from_attributes=True
            )
            for obj in responce.OrderSchemasArray
        ]

    async def set_status(self, orderId: int, newStatus: str) -> None:
        await self.set_status__(
            orderId=orderId,
            newStatus=newStatus
        )

    async def finish_order(self, orderId: int) -> None:
        await self.finish_order__(
            orderId=orderId
        )
