from settings import SecurityConfig

# Encryption
import bcrypt
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
import base64

from .objects import *
from exceptions.token_exceptions import *

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
    
    async def decode_acess_token(token: str) -> JWTInfo:
        if "Bearer" in token:
            token = token[7:]
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
    
    async def decode_basic_token(token: str) -> BaicInfo:
        try:
            token = base64.b64decode(
                token[6:], # delete "Basic " part
                altchars=None,
                validate=False
            ).decode(encoding="utf-8-sig") # decode bytes output

            separator_idx = token.rfind(":") # idx of last ":", which is separator between email and password
            
            return BaicInfo.set_from_dict(
                {
                    "email": token[:separator_idx],
                    "password": token[separator_idx+1:]
                }
            )
        except Exception as exc:
            raise CantDecodeBasicToken(
                description="Can't decode Basic token"
            )