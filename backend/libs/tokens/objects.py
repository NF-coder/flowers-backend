from dataclasses import dataclass

from typing import Dict
from exceptions.token_exceptions import *

from typing_extensions import Self

from pydantic import BaseModel, Field, field_validator

class JWTInfo(BaseModel):
    id: int
    email: str
    expires: int
    type: str
    isEmailConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @staticmethod
    def set_from_dict(data: Dict[str, str]) -> Self:
        '''
            Sets information about token from dict
        '''
        try:
            return JWTInfo(
                email = data["email"],
                id = data["id"],
                expires = data["exp"],
                type = data["type"],
                isEmailConfirmed = data["isEmailConfirmed"],
                isSupplierStatusConfirmed = data["isSupplierStatusConfirmed"],
                isAdmin = data["isAdmin"]
            )
        except Exception as exc:
            raise CantDecodeJWT(
                description="JWT payload dict keys mismatch"
            )    

class BaicInfo(BaseModel):
    email: str
    password: str

    @staticmethod
    def set_from_dict(data: Dict[str, str]) -> Self:
        '''
            Sets information about token from dict
        '''
        try:
            return BaicInfo(
                email = data["email"],
                password = data["password"]
            )
            
        except Exception as exc:
            raise CantDecodeBasicToken(
                description="Basic token payload dict keys mismatch"
            )