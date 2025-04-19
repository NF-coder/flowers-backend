from pydantic import BaseModel

class AddAuthMethodReq(BaseModel):
    tgId: int
    userId: int

class RemoveAuthMethodReq(BaseModel):
    tgId: int
    userId: int

class EmptyModel(BaseModel):
    pass

class TgIdReq(BaseModel):
    tgId: int

class UserIdResp(BaseModel):
    userId: int