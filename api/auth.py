from fastapi import APIRouter, Header, Body
from typing import Dict, Any, Annotated

from settings import MainConfig
from validation.auth import signInModels, confirmEmailModels, registerBasicModels

from libs.database import *
from libs.tokens import Tokens

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/auth",
    tags=["auth"]
)

@router.post("/signIn", tags = ["auth"], status_code=201)
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
    API = await Users.start()
    
    isCrrectPassword = await API.check_password_by_email(
        email=decoded_auth_info.email,
        password=decoded_auth_info.password
    )
    if not isCrrectPassword:
        raise BasicException(
            code=400,
            description="Incorrect password"
        )
    
    user = await API.get_by_email(decoded_auth_info.email)

    token, _ = await Tokens.get_acess_token(
        id=user["id"],
        email=user["email"],
        type=user["type"],
        isEmailConfirmed=user["isEmailConfirmed"],
        isSupplierStatusConfirmed=user["isSupplierStatusConfirmed"]
    )
    
    return {
        "token": token
    }

@router.post("/registerBasic", tags = ["auth"], status_code=201)
async def register(
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

    API = await Users.start()
    
    await API.register(request_body.email, request_body.password, request_body.type)

    user = await API.get_by_email(request_body.email)
    token, _ = await Tokens.get_acess_token(
        id=user["id"],
        email=user["email"],
        type=user["type"],
        isEmailConfirmed=user["isEmailConfirmed"],
        isSupplierStatusConfirmed=user["isSupplierStatusConfirmed"]
    )
    return {"token": token}


# TODO: rewrite this
@router.post("/confirmEmail", tags = ["auth"], status_code=201)
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
        request_headers.Authorization[7:]
    )

    API = await Users.start()
    
    await API.set_email_confirmation_status(
        id = decoded_auth_info.id
    )

    user = await API.get_by_id(decoded_auth_info.id)

    token, _ = await Tokens.get_acess_token(
        id=user["id"],
        email=user["email"],
        type=user["type"],
        isEmailConfirmed=user["isEmailConfirmed"],
        isSupplierStatusConfirmed=user["isSupplierStatusConfirmed"]
    )
    
    return {
        "token": token
    }


# TODO: rewrite this
@router.delete("/deleteUser", tags = ["auth"], status_code=201)
async def deleteUser(
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

    API = await Users.start()
    
    await API.register(request_body.email, request_body.password, request_body.type)

    user = await API.get_by_email(request_body.email)
    token, _ = await Tokens.get_acess_token(
        id=user["id"],
        email=user["email"],
        type=user["type"],
        isEmailConfirmed=user["isEmailConfirmed"],
        isSupplierStatusConfirmed=user["isSupplierStatusConfirmed"]
    )
    return {"token": token}