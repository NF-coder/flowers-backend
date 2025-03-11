from settings import SecurityConfig

# Encryption
import bcrypt
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
import base64

from .objects import *
from exceptions.token_exceptions import *

import traceback
from typing_extensions import Self

class Tokens():
    @staticmethod
    def __init__(self): pass

    async def get_acess_token(**kwargs) -> str:
        exp = int(
                datetime.timestamp(
                    datetime.now(timezone.utc) + timedelta(minutes=SecurityConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
                )
            )
        payload = kwargs
        payload["exp"] = exp

        return jwt.encode(payload, key = SecurityConfig.SECURITY_KEY, algorithm = SecurityConfig.ALGORYTM), exp
    
    # why static analizer does not sees JWTInfo object?
    async def decode_acess_token(token: str) -> JWTInfo:
        token = token[7:] if "Bearer" in token else token
        try:
            payload = jwt.decode(
                token,
                key = SecurityConfig.SECURITY_KEY,
                algorithms = [SecurityConfig.ALGORYTM]
            )

            return JWTInfo.set_from_dict(
                payload
            )
        except Exception as e:
            raise CantDecodeJWT(
                description="Can't decode JWT. Maybe it expired"
            )
    
    async def checkPremissions(
        token,
        isAdmin: bool = False,
        isConfirmedSupplier: bool = False,
        isEmailConfirmed: bool = False
    ) -> None:

        if isAdmin and not token.isAdmin:
            raise NotEnoughPremissions(
                description="You should be admin!"
            )
        
        if isConfirmedSupplier and\
            not token.type == "supplier" and\
            not token.isSupplierStatusConfirmed:
            raise NotEnoughPremissions(
                description="You should be supplier and may have supplier status confirmed!"
            )
        
        if isEmailConfirmed and token.isEmailConfirmed:
            raise NotEnoughPremissions(
                description="Your email should be confirmed!"
            )

    async def decode_basic_token(token: str) -> BaicInfo:
        try:
            token = token[6:] if "Basic" in token else token
            token = base64.b64decode(
                token, # delete "Basic " part
                altchars=None,
                validate=False
            ).decode(encoding="UTF-8-SIG") # decode bytes output

            separator_idx = token.rfind(":") # idx of last ":", which is separator between email and password
            
            return BaicInfo(
                email = token[:separator_idx],
                password = token[separator_idx+1:]
            )
        except Exception as exc:
            raise CantDecodeBasicToken(
                description="Can't decode Basic token"
            )