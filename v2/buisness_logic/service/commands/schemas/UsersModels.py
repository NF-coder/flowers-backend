from pydantic import BaseModel

class User(BaseModel):
    id: int
    type: str
    isConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

class UsersArray(BaseModel):
    usersArray: list[User]

class UserId(BaseModel):
    userId: int