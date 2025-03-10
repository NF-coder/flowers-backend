from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

from ...database.fields.UsersDB import UsersDB

class UserDTO(BaseModel):
    userId: int
    email: str
    type: str
    isEmailConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @staticmethod
    async def parse(obj: UsersDB) -> Self:
        return UserDTO(
            id=obj.id,
            email=obj.email,
            type=obj.type,
            isEmailConfirmed=obj.isEmailConfirmed,
            isSupplierStatusConfirmed=obj.isSupplierStatusConfirmed,
            isAdmin=obj.isAdmin
        )