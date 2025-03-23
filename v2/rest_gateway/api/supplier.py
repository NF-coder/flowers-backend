from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig
from validation.supplier import addProductModels, myProductsListModels, setOrderStatusModels, finishOrderModels, supplierReportModels

#for fustfunc endpoint
from validation.order import OrdersForMeModels

from libs.tokens import Tokens

from exceptions.basic_exception import BasicException

from libs.middleware.logic.Supplier import SupplierLogic
from libs.middleware.logic.Catalog import CatalogLogic

router = APIRouter(
    prefix="/supplier",
    tags=["supplier"]
)

@router.post(
    "/addProduct",
    tags=["supplier"],
    summary="Добавление товара",
    status_code=201
)
async def addProduct(
        request_header: Annotated[addProductModels.RequestHeaderModel, Header()],
        request_body: Annotated[addProductModels.RequestBodyModel, Body()],
    ) -> addProductModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )
    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isConfirmedSupplier=True
    )

    await SupplierLogic.add_product(
        title=request_body.title,
        titleImageUrl=request_body.titleImage,
        costNum=request_body.cost.costNum,
        description=request_body.description,
        authorId=decoded_auth_info.id,
        additionalImagesUrls=request_body.additionalImages
    )

    return addProductModels.ResponceSchema()

@router.get(
    "/myProductsList",
    summary="Просмотр моих товаров",
    tags=["supplier"],
    status_code=200
)
async def myProductsList(
        request_header: Annotated[myProductsListModels.RequestHeaderModel, Header()],
        request_query: Annotated[myProductsListModels.RequestQueryModel, Query()],
    ) -> List[myProductsListModels.ResponceItemSchema]:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )
    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isConfirmedSupplier=True
    )
    
    productArr = await SupplierLogic.my_products_list(
        userId=decoded_auth_info.id,
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )

    return [
        await myProductsListModels.ResponceItemSchema.parse(elem)
        for elem in productArr
    ]

@router.get(
    "/ordersForMe",
    summary="Заказы, которые сделали пользователи",
    tags=["supplier"],
    status_code=200
)
async def ordersForMe(
        request_header: Annotated[OrdersForMeModels.OrdersForMeHeader, Header()],
    ) -> List[OrdersForMeModels.ResponceItemSchema]:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )
    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isConfirmedSupplier=True
    )
    
    myProductsArr = await SupplierLogic.orders_for_me(
        userId=decoded_auth_info.id
    )

    return [
        await OrdersForMeModels.ResponceItemSchema.parse(elem)
        for elem in myProductsArr
    ]

@router.post(
    "/setOrderStatus",
    summary="Установка статуса обработки заказа",
    tags=["supplier"],
    status_code=200
)
async def setOrderStatus(
        request_header: Annotated[setOrderStatusModels.RequestHeaderModel, Header()],
        request_query: Annotated[setOrderStatusModels.RequestQueryModel, Query()],
        request_body: Annotated[setOrderStatusModels.RequestBodyModel, Body()],
    ) -> setOrderStatusModels.ResponceSchema:
    
    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )
    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isConfirmedSupplier=True
    )
    
    await SupplierLogic.set_status(
        orderId=request_query.orderId,
        newStatus=request_body.newStatus
    )

    return setOrderStatusModels.ResponceSchema()

@router.post(
    "/finishOrder",
    summary="Завершение заказа",
    tags=["supplier"],
    status_code=200
)
async def finishOrder(
        request_header: Annotated[finishOrderModels.RequestHeaderModel, Header()],
        request_query: Annotated[finishOrderModels.RequestQueryModel, Query()],
    ) -> finishOrderModels.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_header.Authorization
    )
    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isConfirmedSupplier=True
    )
    
    await SupplierLogic.finish_order(
        orderId=request_query.orderId
    )

    return finishOrderModels.ResponceSchema()

#@router.get("/supplierReport", tags = ["supplier"], status_code=200)
#async def supplierReport(
#        request_query: Annotated[supplierReportModels.RequestQueryModel,Query()],
#        request_header: Annotated[supplierReportModels.RequestHeaderModel, Header()]
#    ) -> List:
#    decoded_auth_info = await Tokens.decode_acess_token(
#        request_header.Authorization
#    )
#    await Tokens.checkPremissions(
#        token=decoded_auth_info,
#        isConfirmedSupplier=True
#    )
#    
#    OrderAPI = await Order.start()
#    CatalogAPI = await Catalog.start()
#
#    if request_query.productId is None:
#        myProductsArr = await CatalogAPI.get_my_products(userId=decoded_auth_info.id, start=0, count=1000, sort="time_descending")
#    else: myProductsArr = [request_query.productId]
#
#    orders = []
#    for product in myProductsArr:
#        orders.extend(
#            await OrderAPI.get_active_with_productId(
#                productId=product["id"]
#            )
#        )
#    
#    out = []
#    for order in orders:
#        date = order["orderCreatedTime"].strftime('%d-%m-%Y')
#        cost = await CatalogAPI.get_product_by_id(id=order["productId"])
#        out.append(
#            {
#                "ID Заявки": order["id"],
#                "Дата создания (UTC)": date,
#                "ID Товара": order["productId"],
#                "Сумма": cost["cost"],
#                "Валюта": "RUB",
#                "Статус оплаты": "Оплата успешно проведена банком " + date,
#                "Комментарий банка": "Это тестовая версия отчёта"
#            }
#        )
#    return out