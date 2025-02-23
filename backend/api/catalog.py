from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List

from settings import MainConfig
from validation.supplier import addProductModels, myProductsListModels

from libs.database import Catalog
from libs.database import ProductAdditionalImages

from libs.tokens import Tokens

from api.serializers import myProductsListSerializer

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/catalog",
    tags=["supplier"]
)

@router.get("/getCatalogItemDetails", tags = ["catalog"], status_code=200)
async def getCatalogItemDetails(
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