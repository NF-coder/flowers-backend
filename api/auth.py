from fastapi import APIRouter, Header
from typing import Dict, Any, Annotated

from settings import MainConfig
#from validation import AuthModels

# from libs.database import *
# from libs.tokens import *

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/auth",
    tags=["auth"]
)


@router.post("/signIn", tags = ["auth"], status_code=201)
async def test(
    Authorization: Annotated[str, Header()],
    ):
    return {
        "out": Authorization
    }

@router.post("/register", tags = ["auth"], status_code=201)
async def register(
    Authorization: AuthModels.SignIn[Any, Any]
    ):
    '''
        POST reqest wich implements registration
        Input:
            login - unique login
            password - password
        Output:
            jwt_token - jwt token
    '''
    await Validators.val_register(**payload)

    API = await Users.start()
    await API.register(**payload)

    user = (await API.get_by_login(payload["login"]))[0]

    token = (await Tokens.get_acess_token(user["login"], user["id"]))[0]
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