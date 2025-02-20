from fastapi import APIRouter, Header, Body
from typing import Dict, Any, Annotated

from settings import MainConfig
#from validation.auth import signInModels, confirmEmailModels, registerBasicModels, deleteUserModels

#from libs.database import 
from libs.tokens import Tokens

from exceptions.basic_exception import BasicException

router = APIRouter(
    prefix=f"/api/v{MainConfig.API_VERSION}/admin",
    tags=["admin"]
)

#@router.post("/listSuppliersRequests", tags = ["auth"], status_code=201)