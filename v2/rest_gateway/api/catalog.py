from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from validation.catalog import getCatalogModels, getCatalogItemDetailsModels, searchModels
from validation.components import CostDict, ReviewsDict

from exceptions.basic_exception import BasicException

from simple_rpc import *

from .commands.CatalogCommands import CatalogCommands

router = APIRouter(
    prefix="/catalog",
    tags=["catalog"]
)

client = GrpcClient(
    port=50513,
    proto_file_relpath="api/protos/CatalogLogic.proto"
)
commands = CatalogCommands(
    client = client
)

@router.get(
    "/getCatalogItemDetails",
    tags=["catalog"],
    summary="Получение деталей о товаре",
    status_code=200
)
async def getCatalogItemDetails(
        request_query: Annotated[getCatalogItemDetailsModels.RequestModel, Query()],
    ) -> getCatalogItemDetailsModels.ResponceSchema:
    
    item = await commands.get_catalog_item_details(
        productId=request_query.id
    )

    return await getCatalogItemDetailsModels.ResponceSchema.parse(
        CatalogObj=item
    ) 

@router.get(
    "/getCatalog",
    tags=["catalog"],
    summary="Каталог товаров",
    status_code=200
)
async def getCatalog(
        request_query: Annotated[getCatalogModels.RequestQueryModel, Query()],
    ) -> List[getCatalogModels.ResponceSchemaItem]:

    productArr = await commands.get_catalog(
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )
    return [
        await getCatalogModels.ResponceSchemaItem.parse(
            CatalogObj=product
        )
        for product in productArr
    ]

# TODO: rewrite func
@router.get("/search", tags = ["catalog"], status_code=200)
async def search(
        request_query: Annotated[searchModels.RequestQueryModel, Query()],
    ) -> List[searchModels.ResponceSchemaItem]:

    productArr = await CatalogLogic.search(
        req=request_query.request,
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )

    return [
        await searchModels.ResponceSchemaItem.parse(
            CatalogObj=product
        )
        for product in productArr
    ]