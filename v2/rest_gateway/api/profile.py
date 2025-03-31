'''
    ## UNSAFE!
    ASAP rewrite to SessionId(Redis) inside JWT auth
'''
from fastapi import APIRouter, Header, Body
from typing import Dict, Any, Annotated

from tokens import Tokens

from exceptions.basic_exception import BasicException

from simple_rpc import *

from .commands.ProfileCommands import ProfileCommands

from validation.profile import deleteUserModels, getProfileBasics


router = APIRouter(
    prefix="/profile",
    tags=["profile"]
)

client = GrpcClient(
    port=50516,
    ip="buisness_logic",
    proto_file_relpath="api/protos/ProfileLogic.proto"
)
commands = ProfileCommands(
    client = client
)

@router.delete(
    "/delete",
    summary="Удаление пользователя",
    tags=["profile"],
    status_code=200
)
async def deleteUser(
        request_headers: Annotated[deleteUserModels.RequestModel, Header()],
    ) -> deleteUserModels.ResponceSchema:
    '''
        POST reqest wich implements deletion of user. Must be initiated by user
        Args:
            request_headers (deleteUserModels.RequestModel):
                Request header which contains JWT token. For more information see `deleteUserModels.RequestModel`
        Returns:
            status (deleteUserModels.ResponceSchema):
                Response with deletion status. For more inforamtion see `deleteUserModels.ResponceSchema`
        Raises:
            BasicException: for all possible errors
    '''

    decoded_auth_info = await Tokens.decode_acess_token(
        request_headers.HTTPBearer
    )

    # DO NOT DELETE BY ID!!! It may cause security vulnerability because we can't deactivate JWT token and user can delete somone else!
    # solution: redis SessionID
    await commands.delete_user(
        userId=decoded_auth_info.id
    )  

    return deleteUserModels.ResponceSchema()

@router.get(
    "/",
    summary="Получение данных о пользователе",
    tags=["profile"],
    status_code=200
)
async def get_user_info(
        request_headers: Annotated[getProfileBasics.RequestModel, Header()],
    ) -> getProfileBasics.ResponceSchema:

    decoded_auth_info = await Tokens.decode_acess_token(
        request_headers.HTTPBearer
    )

    await commands.get_user_info(
        userId=decoded_auth_info.id
    )  

    return deleteUserModels.ResponceSchema()