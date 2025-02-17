from .security.secutity import Security as SequritySettings

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
                    datetime.now(timezone.utc) + timedelta(minutes=SequritySettings.ACCESS_TOKEN_EXPIRE_MINUTES)
                )
            )
        encode = {
            "id": id,
            "expires": exp
        }
        return jwt.encode(encode, key = SequritySettings.SECURITY_KEY, algorithm = SequritySettings.ALGORYTM), exp
    
    async def decode_acess_token(token, info_mode: bool = False) -> str:
        try:
            payload = jwt.decode(token, key = SequritySettings.SECURITY_KEY, algorithms = [SequritySettings.ALGORYTM])
            #login, uid, expires = payload["login"], payload["id"], payload["expires"]
            
            #if login is None or uid is None: raise Exception("Can't decode jwt")
            #if not info_mode: token, expires = await Tokens.get_acess_token(login, uid)

            return payload
        except: raise Exception("Can't decode jwt")