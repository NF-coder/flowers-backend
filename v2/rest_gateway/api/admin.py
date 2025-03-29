from fastapi import APIRouter, Header, Body, Query
from typing import Dict, Any, Annotated, List
from validation.admin import listSuppliersRequestsModels, approveSuppliersRequestModels

from tokens import Tokens

from exceptions.basic_exception import BasicException

from simple_rpc import *

from .commands.AdminCommands import AdminCommands

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

client = GrpcClient(
    port=50511,
    proto_file_relpath="api/protos/AdminLogic.proto"
)
commands = AdminCommands(
    client = client
)

@router.get(
    "/listSuppliersRequests",
    tags=["admin"],
    summary="Список заявок на добавление поставщиков",
    status_code=200
)
async def listSuppliersRequests(
        request_headers: Annotated[listSuppliersRequestsModels.RequestHeaderModel, Header()],
        request_query: Annotated[listSuppliersRequestsModels.RequestQueryModel, Query()]
    ) -> List[listSuppliersRequestsModels.ResponceSchemaItem]:
    '''
        GET reqest wich implements list of unconfirmed suppliers
        TODO: Rewrite this to use another database
        Args:
            request_headers (listSuppliersRequestsModels.RequestHeaderModel):
                Request header which contains Bearer auth token. For more information
                see `listSuppliersRequestsModels.RequestHeaderModel`
            request_query  (listSuppliersRequestsModels.RequestQueryModel):
                Request header which contains query parameters of request. For more information
                see `listSuppliersRequestsModels.RequestQueryModel`
        Returns:
            token (listSuppliersRequestsModels.ResponceSchemaItem):
                Response with list of users. For more inforamtion see `listSuppliersRequestsModels.ResponceSchemaItem`
        Raises:
            BasicException: for all possible errors
    '''
    decoded_auth_info = await Tokens.decode_acess_token(
        request_headers.Authorization
    )
    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isAdmin=True
    )

    users_array = await commands.list_suppliers_requests(
        start=request_query.start,
        count=request_query.count,
        sort=request_query.sort
    )

    return [
        await listSuppliersRequestsModels.ResponceSchemaItem.parse(
            UserObj=user
        )
        for user in users_array
    ]

@router.post(
    "/approveSupplierRequest",
    tags=["admin"],
    summary="Одобрение заявки от поставщика",
    status_code=200
)
async def approveSupplierRequest(
        request_headers: Annotated[approveSuppliersRequestModels.RequestHeaderModel, Header()],
        request_body: Annotated[approveSuppliersRequestModels.RequestBodyModel, Body()]
    ) -> approveSuppliersRequestModels.ResponceSchema:
    '''
        POST reqest wich implements confirmation of supplier
        TODO: Rewrite validation?
        Args:
            request_headers (approveSuppliersRequestModels.RequestHeaderModel):
                Request header which contains Bearer auth token. For more information
                see `approveSuppliersRequestModels.RequestHeaderModel`
            request_body (approveSuppliersRequestModels.RequestBodyModel):
                Request body which contains parameters of request. For more information
                see `approveSuppliersRequestModels.RequestBodyModel`
        Returns:
            token (approveSuppliersRequestModels.ResponceSchema):
                Response with operation status. For more inforamtion see `approveSuppliersRequestModels.ResponceSchema`
        Raises:
            BasicException: for all possible errors
    '''
    decoded_auth_info = await Tokens.decode_acess_token(
        request_headers.Authorization
    )

    await Tokens.checkPremissions(
        token=decoded_auth_info,
        isAdmin=True
    )

    await commands.approve_supplier_request(
        id=request_body.id
    )

    return approveSuppliersRequestModels.ResponceSchema()