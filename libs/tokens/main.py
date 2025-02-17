from settings.main import SecuritySettings

# Encryption
import bcrypt
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError

class Tokens():
    @staticmethod
    def __init__(self): pass

    async def get_acess_token(login: str, id: int) -> str:
        exp = int(
                datetime.timestamp(
                    datetime.now(timezone.utc) + timedelta(minutes=SecuritySettings.ACCESS_TOKEN_EXPIRE_MINUTES)
                )
            )
        encode = {
            "id": id,
            "expires": exp
        }
        return jwt.encode(encode, key = SecuritySettings.SECURITY_KEY, algorithm = SecuritySettings.ALGORYTM), exp
    
    async def decode_acess_token(token) -> str:
        try:
            payload = jwt.decode(token, key = SecuritySettings.SECURITY_KEY, algorithms = [SecuritySettings.ALGORYTM])
            #login, uid, expires = payload["login"], payload["id"], payload["expires"]
            
            #if login is None or uid is None: raise Exception("Can't decode jwt")
            #if not info_mode: token, expires = await Tokens.get_acess_token(login, uid)

            return payload
        except: raise Exception("Can't decode jwt")