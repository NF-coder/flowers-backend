from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

from ...main.schemas.UsersSchemas import UserDTO

class UserSchema(BaseModel):
    userId: int
    email: str
    type: str
    isEmailConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @staticmethod
    async def parse(obj: UserDTO) -> Self:
        return UserSchema(
            userId=obj.userId,
            email=obj.email,
            type=obj.type,
            isEmailConfirmed=obj.isEmailConfirmed,
            isSupplierStatusConfirmed=obj.isSupplierStatusConfirmed,
            isAdmin=obj.isAdmin
        )