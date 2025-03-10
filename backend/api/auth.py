'''
    ## UNSAFE!
    ASAP rewrite to SessionId(Redis) inside JWT auth
'''
from fastapi import APIRouter, Header, Body
from typing import Dict, Any, Annotated

from settings import MainConfig
from validation.auth import signInModels, confirmEmailModels, registerBasicModels, deleteUserModels


from libs.middleware.logic.Auth import AuthLogic
from libs.tokens import Tokens

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# +
@router.post(
    "/signIn",
    tags=["auth"],
    summary="Авторизация",
    status_code=200
)
async def signIn(
        request_headers: Annotated[signInModels.RequestModel, Header()],
    ) -> signInModels.ResponceSchema:
    '''
        POST reqest wich implements sign-in    
        Args:
            request_headers (signInModels.RequestModel):
                Request header which contains Basic auth token. For more information see `signInModels.RequestModel` + read in google
        Returns:
            token (signInModels.ResponceSchema):
                Response with JWT token. For more inforamtion see `signInModels.ResponceSchema`
        Raises:
            BasicException: for all possible errors
    '''
    decoded_auth_info = await Tokens.decode_basic_token(
        request_headers.Authorization
    )
    
    user = await AuthLogic.sign_in(
        email=decoded_auth_info.email,
        password=decoded_auth_info.password
    )
    token, _ = await Tokens.get_acess_token(**user.model_dump())
    
    return signInModels.ResponceSchema(
        token=token
    )

# +
@router.post(
    "/registerBasic",
    tags=["auth"],
    summary="Регистрация",
    status_code=201
)
async def registerBasic(
        request_body: Annotated[registerBasicModels.RequestModel, Body()],
    ) -> registerBasicModels.ResponceSchema:
    '''
        POST reqest wich implements registration
        Args:
            request_body (registerBasicModels.RequestModel):
                Request body which contains `email`, `password` and `type`. For more information see `registerBasicModels.RequestModel`
        Returns:
            token (registerBasicModels.ResponceSchema):
                Response with JWT token. For more inforamtion see `registerBasicModels.ResponceSchema`
        Raises:
            BasicException: for all possible errors
    '''

    user = await AuthLogic.register(
        email=request_body.email,
        password=request_body.password,
        type=request_body.type
    )
    token, _ = await Tokens.get_acess_token(**user.model_dump())

    return registerBasicModels.ResponceSchema(
        token=token
    )


# TODO: rewrite this
# +
@router.post(
    "/confirmEmail",
    tags = ["auth"],
    summary="Подтверждение почты при регистрации (TODO: и её изменении) [всё ещё не реализовано]",
    status_code=200
)
async def confirmEmail(
        request_headers: Annotated[confirmEmailModels.RequestHeaderModel, Header()],
        request_body: Annotated[confirmEmailModels.RequestBodyModel, Body()]
    ) -> confirmEmailModels.ResponceSchema:
    '''
        POST reqest wich implements email verification

        ### IMPORTANT!
        There's no time to work with email confirmation, so any confirmation code is correct

        Args:
            request_headers (confirmEmailModels.RequestHeadersModel):
                Request header which contains JWT auth token. For more information see `confirmEmailModels.RequestHeadersModel`
            request_body (confirmEmailModels.RequestBodyModel):
                Request body which email confirmation code. For more information see `confirmEmailModels.RequestBodyModel`
        Returns:
            token (confirmEmailModels.ResponceSchema):
                Response with JWT token. For more inforamtion see `confirmEmailModels.ResponceSchema`
        Raises:
            BasicException: for all possible errors
    '''
    decoded_auth_info = await Tokens.decode_acess_token(
        request_headers.Authorization
    )
    
    user = await AuthLogic.register(id=decoded_auth_info.id)
    token, _ = await Tokens.get_acess_token(**user.model_dump())
    
    return confirmEmailModels.ResponceSchema(
        token=token
    )

# Can create security issues!
# DO NOT USE THIS ENDPOINT BEFORE I FIX PROBLEMS WITH DB
# +
#@router.delete("/deleteUser", tags = ["auth"], status_code=201)
#async def deleteUser(
#        request_header: Annotated[deleteUserModels.RequestModel, Header()],
#    ) -> deleteUserModels.ResponceSchema:
#    '''
#        POST reqest wich implements deletion of user. Must be initiated by user
#        Args:
#            request_header (deleteUserModels.RequestModel):
#                Request header which contains JWT token. For more information see `deleteUserModels.RequestModel`
#        Returns:
#            status (deleteUserModels.ResponceSchema):
#                Response with deletion status. For more inforamtion see `deleteUserModels.ResponceSchema`
#        Raises:
#            BasicException: for all possible errors
#    '''
#
#    decoded_auth_info = await Tokens.decode_acess_token(
#        request_header.Authorization[7:]
#    )
#
#    # DO NOT DELETE BY ID!!! It may cause security vulnerability because we can't deactivate JWT token and user can delete somone else!
#    await UsersAPI.delete_user_by_email(
#        decoded_auth_info.email
#    )  
#
#    return deleteUserModels.ResponceSchema()