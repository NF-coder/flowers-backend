from dataclasses import dataclass

from typing import Dict
from exceptions.token_exceptions import *

from typing import Self

@dataclass
class JWTInfo:
    id: str
    email: str
    expires: int
    type: str
    isEmailConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @classmethod
    def set_from_dict(self, data: Dict[str, str]) -> Self:
        '''
            Sets information about token from dict
        '''
        try:
            self.email = data["email"]
            self.id = data["id"]
            self.expires = data["exp"]
            self.type = data["type"]
            self.isEmailConfirmed = data["isEmailConfirmed"]
            self.isSupplierStatusConfirmed = data["isSupplierStatusConfirmed"]
            self.isAdmin = data["isAdmin"]
        except Exception as exc:
            raise CantDecodeJWT(
                description="JWT payload dict keys mismatch"
            )
        
        return self

@dataclass
class BaicInfo:
    email: str
    password: str

    @classmethod
    def set_from_dict(self, data: Dict[str, str]) -> Self:
        '''
            Sets information about token from dict
        '''
        try:
            self.email = data["email"]
            self.password = data["password"]
        except Exception as exc:
            raise CantDecodeBasicToken(
                description="Basic token payload dict keys mismatch"
            )
        
        return self