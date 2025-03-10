from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig

from validation.catalog import getCatalogModels, getCatalogItemDetailsModels, searchModels
from validation.components import CostDict, ReviewsDict

from libs.middleware.logic.Catalog import CatalogLogic

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/catalog",
    tags=["catalog"]
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
    
    item = await CatalogLogic.get_catalog_item_details(
        id=request_query.id
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

    productArr = await CatalogLogic.get_catalog(
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

# +
#@router.get("/search", tags = ["catalog"], status_code=200)
#async def search(
#        request_query: Annotated[searchModels.RequestQueryModel, Query()],
#    ) -> List[searchModels.ResponceSchemaItem]:
#
#    productArr = await CatalogLogic.search_in_title(
#        phrase=request_query.request,
#        start=request_query.start,
#        count=request_query.count,
#        sort=request_query.sort
#    )
#
#    return [
#        await getCatalogModels.ResponceSchemaItem.parse(
#            CatalogObj=product
#        )
#        for product in productArr
#    ]
#
#    serializer = await searchSerializer.start()
#    print([await serializer.serializeItem(elem) for elem in productArr])
#    return [await serializer.serializeItem(elem) for elem in productArr]