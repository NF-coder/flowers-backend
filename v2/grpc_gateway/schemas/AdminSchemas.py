from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

#from .UsersSchemas import UserDTO

class UserSchema(BaseModel):
    userId: int
    type: str
    isConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @staticmethod
    async def parse(obj) -> Self:
        return UserSchema(
            userId=obj.userId,
            type=obj.type,
            isConfirmed=obj.isConfirmed,
            isSupplierStatusConfirmed=obj.isSupplierStatusConfirmed,
            isAdmin=obj.isAdmin
        )