from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from validation.order import CreateOrderModels, OrderInfoModels, myActiveOrdersModels, CancelOrderModels

from tokens import Tokens

from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient

from .commands.OrderCommands import OrderCommands

router = APIRouter(
    prefix="/order",
    tags=["order"]
)

client = GrpcClient(
    port=50514,
    ip="buisness_logic",
    proto_file_relpath="api/protos/OrderLogic.proto"
)
commands = OrderCommands(
    client = client
)

@router.post(
    "/create",
    tags=["order"],
    summary="Создание заказа",
    status_code=201
)
async def createOrder(
        request_header: Annotated[CreateOrderModels.CreateOrderHeaderModel, Header()],
        request_body: Annotated[CreateOrderModels.CreateOrderBody, Body()],
    ) -> CreateOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.HTTPBearer
    )

    await commands.create_order(
        country=request_body.Geo.Country,
        city=request_body.Geo.City,
        street=request_body.Geo.Street,
        building=request_body.Geo.Building,
        flat=request_body.Geo.Flat,

        userId=decoded_auth_info.id,

        firstName=request_body.FirstName,
        secondName=request_body.SecondName,
        comment=request_body.Comment,
        phoneNumber=request_body.PhoneNumber,

        productIdArray=request_body.ProductIdArray
    )

    return CreateOrderModels.ResponceSchema()

@router.get(
    "/list/{order_id}",
    tags=["order"],
    summary="Информация о заказе по идентификатору",
    status_code=200
)
async def orderInfo(
        request_header: Annotated[OrderInfoModels.OrderInfoHeader, Header()],
        order_id: int,
    ) -> OrderInfoModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.HTTPBearer
    )

    orderInfo = await commands.order_info(
        orderId=order_id
    )

    return await OrderInfoModels.ResponceSchema.parse(
        OrderObj=orderInfo
    )


@router.get(
    "/active",
    tags=["order"],
    summary="Информация об активных заказах пользователя",
    status_code=200
)
async def myActiveOrders(
        request_header: Annotated[myActiveOrdersModels.MyActiveOrdersHeader, Header()],
    ) -> List[myActiveOrdersModels.ResponceItemSchema]:
    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.HTTPBearer
    )
    ordersArr = await commands.get_active_by_userId(
        userId=decoded_auth_info.id
    )
    return [
        await myActiveOrdersModels.ResponceItemSchema.parse(
            OrderObj=orderInfo
        )
        for orderInfo in ordersArr
    ]

@router.post(
    "/cancel/{order_id}",
    tags=["order"],
    summary="Отмена заказа",
    status_code=200
)
async def cancelOrder(
        request_header: Annotated[CancelOrderModels.CancelOrderHeader, Header()],
        order_id: int,
    ) -> CancelOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.HTTPBearer
    )

    await commands.cancel_by_id(
        id=order_id
    )

    return CancelOrderModels.ResponceSchema()