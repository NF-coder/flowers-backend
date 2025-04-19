from typing_extensions import Self, Literal, Optional
from pydantic import BaseModel, Field

class UserIdModel(BaseModel):
    userId: int

class IsIdRegistredRes(BaseModel):
    state: bool

class EmptyModel(BaseModel):
    pass

class FindUnconfirmedSuppliers(BaseModel):
    start: int
    count: int
    sort: str

class AddNewUserRequest(BaseModel):
    type: str = Literal["supplier", "costumer"]