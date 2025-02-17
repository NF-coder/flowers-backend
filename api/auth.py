from fastapi import APIRouter, Header
from typing import Dict, Any, Annotated

from settings import MainConfig
from validation import AuthModels

from libs.database import *
from libs.tokens import Tokens

from exceptions.database_exceptions import NotUnique
from exceptions.basic_exception import HttpException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/auth",
    tags=["auth"]
)


#@router.post("/signIn", tags = ["auth"], status_code=201)
#async def test(
#        Authorization: Annotated[str, Header()],
#    ):
#    return {
#        "out": Authorization
#    }

@router.post("/registerBasic", tags = ["auth"], status_code=201)
async def register(
        request_body: AuthModels.RegisterBasic,
    ) -> AuthModels.RespSchemaRegisterBasic:
    '''
        POST reqest wich implements registration
        Args:
            request_body (AuthModels.RegisterBasic):
                Request body which contains `email`, `password` and `type`. For more information see `AuthModels.RegisterBasic`
        Returns:
            token (AuthModels.RespSchemaRegisterBasic):
                Response with JWT token. For more inforamtion see `AuthModels.RespSchemaRegisterBasic`
        Raises:
            HttpException: for all possible errors
    '''

    try:
        API = await Users.start()
    except NoDatabaseConnection as exc:
        raise HttpException(
            code=500,
            description=exc.description
        )
    
    try:
        await API.register(request_body.email, request_body.password)
    except NotUnique as exc:
        raise HttpException(
            code=400,
            description=exc.description
        )

    user = await API.get_by_email(request_body.email)

    token = (await Tokens.get_acess_token(user["email"], user["id"]))[0]
    return {"token": token}


#@router.post("/signIn", tags = ["auth"], status_code=200)
#async def login(
#    payload: Annotated[Any, Any]
#):
#    '''
#        POST reqest wich implements sign-in
#        Input:
#            login - login
#            password - password
#        Output:
#            token - jwt token
#    '''
#    await Validators.val_login(login = payload["login"], password = payload["password"])
#
#    API = await Users.start()
#    user = (await API.get_by_login(payload["login"]))[0]
#    del user["password"]
#
#    token = (await Tokens.get_acess_token(user["login"], user["id"]))[0]
#    return {"jwt_token": token}