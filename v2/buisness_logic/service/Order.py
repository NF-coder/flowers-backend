from typing_extensions import List, Self, Optional
from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient, GrpcServer
from commands.OrderCommands import OrderCommands
from commands.GeoCommands import GeoCommands

import asyncio

from input_schemas.Order import *
from output_schemas.OrderSchemas import *

OrdersClient = GrpcClient(
    port=50503,
    ip="order_controller",
    proto_file_relpath="protos/Order.proto"
)
GeoClient = GrpcClient(
    port=50506,
    ip="geo_controller",
    proto_file_relpath="protos/Geo.proto"
)
OrderCommandsManager = OrderCommands(
    client = OrdersClient
)
GeoCommandsManager = GeoCommands(
    client = GeoClient
)
app = GrpcServer()


class OrderLogic():
    def __init__(self) -> None:
        pass
    
    @app.grpc_method()
    async def create_order(
            self,
            request: CreateOrderReq
        ) -> EmptyMessage:
        geoId = await GeoCommandsManager.add_geo(
            country=request.country,
            city=request.city,
            street=request.street,
            building=request.building,
            flat=request.flat,
            userId=request.userId
        )

        for productId in request.productIdArray:
            await OrderCommandsManager.create_order(
                geoId=geoId.id,
                userId=request.userId,
                firstName=request.firstName,
                secondName=request.secondName,
                comment=request.comment,
                phoneNumber=request.phoneNumber,
                productId=productId
            )
        return EmptyMessage()
    
    @app.grpc_method()
    async def order_info(
            self,
            request: OredrIdReq
        ) -> OrderSchema:
        order = await OrderCommandsManager.get_order_by_id(
            id=request.orderId
        )
        geo = await GeoCommandsManager.get_geo_by_id(
            geoId=order.geoId
        )
        return await OrderSchema.parse(order, geo)
    
    @app.grpc_method()
    async def get_active_by_userId(
            self,
            request: UserIdReq
        ) -> OrderSchemasArray:
        orders = await OrderCommandsManager.get_active_orders_by_userid(
            userId=request.userId
        )
        out = []
        for order in orders.OrderDTOArray:
            geo = await GeoCommandsManager.get_geo_by_id(
                geoId=order.geoId
            )
            out.append(
                await OrderSchema.parse(order, geo)
            )
        return OrderSchemasArray(
            OrderSchemasArray=out
        )

app.configure_service(
    cls=OrderLogic(),
    port=50514
)
app.run()