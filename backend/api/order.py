from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig
from validation.order import CreateOrderModels, OrderInfoModels, myActiveOrdersModels, CancelOrderModels, OrdersForMeModels

from libs.database import Order, Geo, OrderProducts, Catalog

from libs.tokens import Tokens

from api.serializers import orderInfoSerializer
from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/order",
    tags=["order"]
)

@router.post("/createOrder", tags = ["catalog"], status_code=202)
async def createOrder(
        request_header: Annotated[CreateOrderModels.CreateOrderHeaderModel, Header()],
        request_body: Annotated[CreateOrderModels.CreateOrderBody, Body()],
    ) -> CreateOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    GeoAPI = await Geo.start()
    geoId = await GeoAPI.add_geo(
        country=request_body.Geo.Country,
        city=request_body.Geo.City,
        street=request_body.Geo.Street,
        building=request_body.Geo.Building,
        flat=request_body.Geo.Flat,
        userId=decoded_auth_info.id
    )

    OrderAPI = await Order.start()
    orderId = await OrderAPI.create_order(
        geoId=geoId,
        userId=decoded_auth_info.id,
        firstName=request_body.FirstName,
        secondName=request_body.SecondName,
        comment=request_body.Comment,
        phoneNumber=request_body.PhoneNumber
    )

    OrderProductsAPI = await OrderProducts.start()
    productsArr = await OrderProductsAPI.add_products(
        userId=decoded_auth_info.id,
        orderId=orderId,
        productIds=request_body.ProductIdArray
    )

    return {"status": "ok"}

@router.get("/orderInfo", tags = ["catalog"], status_code=202)
async def orderInfo(
        request_header: Annotated[OrderInfoModels.OrderInfoHeader, Header()],
        request_query: Annotated[OrderInfoModels.OrderInfoQuery, Query()],
    ) -> OrderInfoModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    OrderAPI = await Order.start()
    orderInfo = await OrderAPI.get_by_id(
        id=request_query.orderId
    )

    serializer = await orderInfoSerializer.start()
    return await serializer.serialize(orderInfo[0])


@router.get("/myActiveOrders", tags = ["catalog"], status_code=202)
async def myActiveOrders(
        request_header: Annotated[myActiveOrdersModels.MyActiveOrdersHeader, Header()],
    ) -> List[myActiveOrdersModels.ResponceItemSchema]:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    OrderAPI = await Order.start()
    orderInfo = await OrderAPI.get_active_by_userId(
        userId=decoded_auth_info.id
    )

    serializer = await orderInfoSerializer.start()
    out = []
    for item in orderInfo:
        print(item)
        out.append(await serializer.serialize(item))
    return out


@router.post("/cancelOrder", tags = ["order"], status_code=202)
async def cancelOrder(
        request_header: Annotated[CancelOrderModels.CancelOrderHeader, Header()],
        request_body: Annotated[CancelOrderModels.CancelOrderBody, Body()],
    ) -> CancelOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    OrderAPI = await Order.start()
    await OrderAPI.cancel_by_id(
        id=request_body.orderId
    )

    return {"status": "ok"}








# fastfunc from supplier
'''
@router.get("/ordersForMe", tags = ["supplier"], status_code=200)
async def ordersForMe(
        request_header: Annotated[OrdersForMeModels.OrdersForMeHeader, Header()],
    ) -> List[OrdersForMeModels.ResponceItemSchema]:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    if not decoded_auth_info.type == "supplier" and\
          not decoded_auth_info.isSupplierStatusConfirmed:
        raise BasicException(
            code=400,
            description="You're not supplier or your supplier status is unconfirmed"
        )
    CatalogAPI = await Catalog.start()
    myProductsArr = await CatalogAPI.get_my_products(userId=decoded_auth_info.id, start=0, count=100, sort="time_descending")

    OrderProductsAPI = await OrderProducts.start()
    orderProductsInfoArr = []
    for productId in myProductsArr:
        orderProductsInfoArr.extend(await OrderProductsAPI.get_by_productId(
            productId=productId
        ))
    
    orderProductsInfoArr = list(set([
        elem["orderId"] for elem in orderProductsInfoArr
    ]))


    serializer = await orderInfoSerializer.start()
    out = []
    for item in orderInfo:
        print(item)
        out.append(await serializer.serialize(item))
    return out
'''