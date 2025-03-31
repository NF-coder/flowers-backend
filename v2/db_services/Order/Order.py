from typing import Self

from exceptions.database_exceptions import *
from settings import DBSettings

from database.OrderAPI import OrderAPI
from database.OrderDB import OrderDB

from schemas.OrderSchemas import *
from schemas.RPCScheams import *

from simple_rpc import GrpcServer

app = GrpcServer()

class Order():
    def __init__(self) -> Self:
        self.OrderAPI = OrderAPI(OrderDB, DBSettings.DATABASE_URL)

    @app.grpc_method()
    async def create_order(
        self,
        request: CreateOrderReq
    ) -> OrderIdModel:
        
        return OrderIdModel(
            id = await self.OrderAPI.create_order(
                geoId=request.geoId,
                userId=request.userId,
                firstName=request.firstName,
                secondName=request.secondName,
                comment=request.comment,
                phoneNumber=request.phoneNumber,
                productId=request.productId
            )
        )
    
    @app.grpc_method()
    async def get_by_id(
        self,
        request: OrderIdModel
    ) -> OrderDTO:
        result = await self.OrderAPI.get_by_id(
            id=request.id
        )
        return await OrderDTO.parse(result)
    
    @app.grpc_method()
    async def get_by_productId(
        self,
        request: ProductIdModel
    ) -> OrderDTOArray:
        result = await self.OrderAPI.get_by_productId(
            productId=request.productId
        )
        return OrderDTOArray(
            OrderDTOArray=[
                await OrderDTO.parse(order)
                for order in result
            ]
        )
    
    @app.grpc_method()
    async def set_status_by_id(
        self,
        request: SetStatusByIdRequest
    ) -> EmptyModel:
        await self.OrderAPI.set_status_by_id(
            id=request.id,
            newStatus=request.newStatus
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def cancel_by_id(
        self,
        request: OrderIdModel
    ) -> EmptyModel:
        await self.OrderAPI.set_cancel_status_by_id(
            id=request.id,
            newStatus=True
        )
        return EmptyModel()

    @app.grpc_method()
    async def finish_by_id(
        self,
        request: OrderIdModel
    ) -> EmptyModel:
        await self.OrderAPI.set_finish_status_by_id(
            id=request.id,
            newStatus=True
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def get_active_by_userId(
        self,
        request: UserIdModel,
    ) -> OrderDTOArray:
        result = await self.OrderAPI.get_active_orders_by_userId(
            userId=request.userId
        )
        return OrderDTOArray(
            OrderDTOArray=[
                await OrderDTO.parse(order)
                for order in result
            ]
        )
    
    @app.grpc_method()
    async def get_all_active(
        self,
        request: EmptyModel
    ) -> OrderDTOArray:
        result = await self.OrderAPI.get_all_active_orders()
        return OrderDTOArray(
            OrderDTOArray=[
                await OrderDTO.parse(order)
                for order in result
            ]
        )

    @app.grpc_method()
    async def get_active_with_productId(
        self,
        request: ProductIdModel
    ) -> OrderDTOArray:
        result = await self.OrderAPI.get_all_active_orders_with_productId(
            productId = request.productId
        )
        return OrderDTOArray(
            OrderDTOArray=[
                await OrderDTO.parse(order)
                for order in result
            ]
        )

# SimpleRPC server startup

app.configure_service(
    cls=Order(),
    port=50503
)
app.run()