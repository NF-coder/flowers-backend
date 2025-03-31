from pydantic import BaseModel

class SignInByEmailReq(BaseModel):
    email: str
    password: str

class RegisterByEmailReq(BaseModel):
    email: str
    password: str
    type: str

class RegisterByTgId(BaseModel):
    tgId: str
    type: str

class TgIdModel(BaseModel):
    tgId: str