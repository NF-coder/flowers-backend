from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

class AddAuthMethodRequest(BaseModel):
    email: str
    userId: int
    password: str

class RemoveAuthMethodRequest(BaseModel):
    email: str

class EmptyResponce(BaseModel):
    pass

class CheckPasswordRequest(BaseModel):
    email: str
    password: str

class CheckPasswordResponce(BaseModel):
    status: str