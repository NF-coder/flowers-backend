from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig
from validation.order import CreateOrderModels, OrderInfoModels, myActiveOrdersModels, CancelOrderModels

from libs.middleware.logic.Order import OrderLogic

from libs.tokens import Tokens

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/order",
    tags=["order"]
)

@router.post("/createOrder", tags = ["order"], status_code=202)
async def createOrder(
        request_header: Annotated[CreateOrderModels.CreateOrderHeaderModel, Header()],
        request_body: Annotated[CreateOrderModels.CreateOrderBody, Body()],
    ) -> CreateOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    OrderLogic.create_order(
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
        productId=request_body.ProductIdArray
    )

    return CreateOrderModels.ResponceSchema()

@router.get("/orderInfo", tags = ["order"], status_code=202)
async def orderInfo(
        request_header: Annotated[OrderInfoModels.OrderInfoHeader, Header()],
        request_query: Annotated[OrderInfoModels.OrderInfoQuery, Query()],
    ) -> OrderInfoModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    orderInfo = await OrderLogic.order_info(
        id=request_query.orderId
    )

    return await OrderInfoModels.ResponceSchema.parse(
        OrderObj=orderInfo
    )


@router.get("/myActiveOrders", tags = ["order"], status_code=202)
async def myActiveOrders(
        request_header: Annotated[myActiveOrdersModels.MyActiveOrdersHeader, Header()],
    ) -> List[myActiveOrdersModels.ResponceItemSchema]:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    ordersArr = await OrderLogic.get_active_by_userId(
        userId=decoded_auth_info.id
    )

    return [
        myActiveOrdersModels.ResponceItemSchema.parse(
            OrderObj=orderInfo
        )
        for orderInfo in ordersArr
    ]

@router.post("/cancelOrder", tags = ["order"], status_code=202)
async def cancelOrder(
        request_header: Annotated[CancelOrderModels.CancelOrderHeader, Header()],
        request_body: Annotated[CancelOrderModels.CancelOrderBody, Body()],
    ) -> CancelOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    await OrderLogic.cancel_by_id(
        id=request_body.orderId
    )

    return CancelOrderModels.ResponceSchema()