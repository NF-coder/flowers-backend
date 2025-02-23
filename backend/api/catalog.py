from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig
from validation.catalog import getCatalogModels, getCatalogItemDetailsModels, searchModels

from libs.database import Catalog
from libs.database import ProductAdditionalImages

from libs.tokens import Tokens

from api.serializers import getCatalogItemDetailsSerializer, getCatalogSerializer, searchSerializer

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/catalog",
    tags=["supplier"]
)

# It not works. Why?
'''
@router.get("/getCatalogItemDetails", tags = ["catalog"], status_code=200)
async def getCatalogItemDetails(
        request_query: Annotated[getCatalogItemDetailsModels.RequestModel, Query()],
    ) -> getCatalogItemDetailsModels.ResponceSchema:
    
    API = await Catalog.start()
    res = await API.get_product_by_id(
        id=request_query.id
    )

    serializer = await getCatalogItemDetailsSerializer.start()
    return await serializer.serialize(res)
'''

@router.get("/getCatalog", tags = ["catalog"], status_code=200)
async def getCatalogItemDetails(
        request_query: Annotated[getCatalogModels.RequestQueryModel, Query()],
    ) -> List[getCatalogModels.ResponceSchemaItem]:

    API = await Catalog.start()
    productArr = await API.get_products(
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )

    serializer = await getCatalogSerializer.start()
    print([await serializer.serializeItem(elem) for elem in productArr])
    return [await serializer.serializeItem(elem) for elem in productArr]

@router.get("/search", tags = ["catalog"], status_code=200)
async def search(
        request_query: Annotated[searchModels.RequestQueryModel, Query()],
    ) -> List[getCatalogModels.ResponceSchemaItem]:

    API = await Catalog.start()
    productArr = await API.search_in_title(
        phrase=request_query.request,
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )

    serializer = await searchSerializer.start()
    print([await serializer.serializeItem(elem) for elem in productArr])
    return [await serializer.serializeItem(elem) for elem in productArr]