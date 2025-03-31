'''
    ## UNSAFE!
    ASAP rewrite to SessionId(Redis) inside JWT auth
'''

from fastapi import APIRouter, Header, Body
from typing import Dict, Any, Annotated

from validation.auth import registerEmailModels, signInEmailModels
from validation.auth import registerTgModels, signInTgModels

from validation.auth import confirmEmailModels

from tokens import Tokens

from exceptions.basic_exception import BasicException

from simple_rpc import *

from .commands.AuthCommands import AuthCommands

from .settings.Settings import TgBotApiAcess


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

client = GrpcClient(
    port=50512,
    ip="buisness_logic",
    proto_file_relpath="api/protos/AuthLogic.proto"
)
commands = AuthCommands(
    client = client
)

# +
@router.post(
    "/sign-in/by-email",
    tags=["auth"],
    summary="Авторизация",
    status_code=200
)
async def signIn_email(
        request_headers: Annotated[signInEmailModels.RequestModel, Header()],
    ) -> signInEmailModels.ResponceSchema:
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
        request_headers.HTTPBearer
    )
    
    user = await commands.sign_in_by_email(
        email=decoded_auth_info.email,
        password=decoded_auth_info.password
    )
    token, _ = await Tokens.get_acess_token(**user.model_dump())
    
    return signInEmailModels.ResponceSchema(
        token=token
    )

# TODO: придумать нормальное ограничение доступа
@router.post(
    "/sign-in/by-tg",
    tags=["auth"],
    summary="Авторизация",
    status_code=200
)
async def signIn_tg(
        request_headers: Annotated[signInTgModels.RequestModel, Header()],
    ) -> signInTgModels.ResponceSchema:
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
    if request_headers.Key != f"{TgBotApiAcess.API_KEY}":
        raise BaseException(
            code=400,
            description="Uncorrect API key!"
        )

    user = await commands.sign_in_by_tgId(
        tgId=request_headers.tgId
    )
    token, _ = await Tokens.get_acess_token(**user.model_dump())
    
    return signInEmailModels.ResponceSchema(
        token=token
    )

# +
@router.post(
    "/register/by-email",
    tags=["auth"],
    summary="Регистрация",
    status_code=201
)
async def register_email(
        request_body: Annotated[registerEmailModels.RequestModel, Body()],
    ) -> registerEmailModels.ResponceSchema:
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

    user = await commands.register_by_email(
        email=request_body.email,
        password=request_body.password,
        type=request_body.type
    )
    token, _ = await Tokens.get_acess_token(**user.model_dump())

    return registerEmailModels.ResponceSchema(
        token=token
    )

# TODO: придумать нормальное ограничение доступа
@router.post(
    "/register/by-tg",
    tags=["auth"],
    summary="Регистрация",
    status_code=201
)
async def register_tg(
        request_headers: Annotated[registerTgModels.RequestHeadersModel, Header()],
        request_body: Annotated[registerTgModels.RequestModel, Body()],
    ) -> registerTgModels.ResponceSchema:
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
    if request_headers.Key != f"{TgBotApiAcess.API_KEY}":
        raise BaseException(
            code=400,
            description="Uncorrect API key!"
        )


    user = await commands.register_by_tgId(
        tgId=request_body.tgId,
        type=request_body.type
    )
    token, _ = await Tokens.get_acess_token(**user.model_dump())

    return registerEmailModels.ResponceSchema(
        token=token
    )