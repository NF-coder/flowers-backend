from pydantic import BaseModel

class SignInByEmailReq(BaseModel):
    email: str
    password: str

class RegisterByEmailReq(BaseModel):
    email: str
    password: str
    type: str

class RegisterByTgId(BaseModel):
    tgId: int
    type: str

class TgIdModel(BaseModel):
    tgId: int