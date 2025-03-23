from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    userId: int
    email: str
    type: str
    isConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @staticmethod
    async def parse(obj) -> Self:
        return UserSchema(
            userId=obj.userId,
            email=obj.email,
            type=obj.type,
            isConfirmed=obj.isConfirmed,
            isSupplierStatusConfirmed=obj.isSupplierStatusConfirmed,
            isAdmin=obj.isAdmin
        )