from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig
from validation.supplier import addProductModels, myProductsListModels, setOrderStatusModels, finishOrderModels, supplierReportModels

from libs.database import Catalog
from libs.database import ProductAdditionalImages

#for fustfunc endpoint
from api.serializers import orderInfoSerializer
from libs.database import Order
from validation.order import OrdersForMeModels

from libs.tokens import Tokens

from api.serializers import myProductsListSerializer

from exceptions.basic_exception import BasicException

from datetime import datetime

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/supplier",
    tags=["supplier"]
)

@router.post("/addProduct", tags = ["supplier"], status_code=200)
async def addProduct(
        request_header: Annotated[addProductModels.RequestHeaderModel, Header()],
        request_body: Annotated[addProductModels.RequestBodyModel, Body()],
    ) -> addProductModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    if not decoded_auth_info.type == "supplier" and\
          not decoded_auth_info.isSupplierStatusConfirmed:
        raise BasicException(
            code=400,
            description="You're not supplier or your supplier status is unconfirmed"
        )
    
    API = await Catalog.start()
    productId = await API.add_product(
        title=request_body.title,
        titleImageUrl=request_body.titleImage,
        costNum=request_body.cost.costNum,
        description=request_body.description,
        authorId=decoded_auth_info.id,
    )
    ImagesAPI = await ProductAdditionalImages.start()
    await ImagesAPI.add_images(
        imageUrls=request_body.additionalImages,
        productId=productId
    )

    return {"status": "ok"}

@router.get("/myProductsList", tags = ["supplier"], status_code=200)
async def myProductsList(
        request_header: Annotated[myProductsListModels.RequestHeaderModel, Header()],
        request_query: Annotated[myProductsListModels.RequestQueryModel, Query()],
    ) -> List[myProductsListModels.ResponceSchemaItem]:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    if not decoded_auth_info.type == "supplier" and\
          not decoded_auth_info.isSupplierStatusConfirmed:
        raise BasicException(
            code=400,
            description="You're not supplier or your supplier status is unconfirmed"
        )
    
    API = await Catalog.start()
    productArr = await API.get_my_products(
        userId=decoded_auth_info.id,
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )

    serializer = await myProductsListSerializer.start()
    print([await serializer.serializeItem(elem) for elem in productArr])
    return [await serializer.serializeItem(elem) for elem in productArr]


# fastfunc from supplier
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
    
    OrderAPI = await Order.start()
    CatalogAPI = await Catalog.start()
    myProductsArr = await CatalogAPI.get_my_products(userId=decoded_auth_info.id, start=0, count=1000, sort="time_descending")

    orderProductsInfoArr = []
    for productId in myProductsArr:
        orderProductsInfoArr.extend(await OrderAPI.get_active_with_productId(
            productId=productId["id"]
        ))

    serializer = await orderInfoSerializer.start()
    out = []
    for item in orderProductsInfoArr:
        out.append(await serializer.serialize(item))
    return out

@router.post("/setOrderStatus", tags = ["supplier"], status_code=200)
async def setOrderStatus(
        request_header: Annotated[setOrderStatusModels.RequestHeaderModel, Header()],
        request_query: Annotated[setOrderStatusModels.RequestQueryModel, Query()],
        request_body: Annotated[setOrderStatusModels.RequestBodyModel, Body()],
    ) -> setOrderStatusModels.ResponceSchema:
    
    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    if not decoded_auth_info.type == "supplier" and\
          not decoded_auth_info.isSupplierStatusConfirmed:
        raise BasicException(
            code=400,
            description="You're not supplier or your supplier status is unconfirmed"
        )
    
    OrderAPI = await Order.start()

    await OrderAPI.set_status_by_id(
        id=request_query.orderId,
        newStatus=request_body.newStatus
    )

    return {"status": "ok"}

@router.post("/finishOrder", tags = ["supplier"], status_code=200)
async def finishOrder(
        request_header: Annotated[finishOrderModels.RequestHeaderModel, Header()],
        request_query: Annotated[finishOrderModels.RequestQueryModel, Query()],
    ) -> finishOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    if not decoded_auth_info.type == "supplier" and\
          not decoded_auth_info.isSupplierStatusConfirmed:
        raise BasicException(
            code=400,
            description="You're not supplier or your supplier status is unconfirmed"
        )
    
    OrderAPI = await Order.start()

    await OrderAPI.finish_by_id(
        id=request_query.orderId
    )

    return {"status": "ok"}

@router.get("/supplierReport", tags = ["supplier"], status_code=200)
async def supplierReport(
        request_query: Annotated[supplierReportModels.RequestQueryModel,Query()],
        request_header: Annotated[supplierReportModels.RequestHeaderModel, Header()]
    ) -> List:
    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )

    if not decoded_auth_info.type == "supplier" and\
          not decoded_auth_info.isSupplierStatusConfirmed:
        raise BasicException(
            code=400,
            description="You're not supplier or your supplier status is unconfirmed"
        )
    
    OrderAPI = await Order.start()
    CatalogAPI = await Catalog.start()

    if request_query.productId is None:
        myProductsArr = await CatalogAPI.get_my_products(userId=decoded_auth_info.id, start=0, count=1000, sort="time_descending")
    else: myProductsArr = [request_query.productId]

    orders = []
    for product in myProductsArr:
        orders.extend(
            await OrderAPI.get_active_with_productId(
                productId=product["id"]
            )
        )
    
    out = []
    for order in orders:
        date = order["orderCreatedTime"].strftime('%d-%m-%Y')
        cost = await CatalogAPI.get_product_by_id(id=order["productId"])
        out.append(
            {
                "ID Заявки": order["id"],
                "Дата создания (UTC)": date,
                "ID Товара": order["productId"],
                "Сумма": cost["cost"],
                "Валюта": "RUB",
                "Статус оплаты": "Оплата успешно проведена банком " + date,
                "Комментарий банка": "Это тестовая версия отчёта"
            }
        )
    return out