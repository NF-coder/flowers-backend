from typing_extensions import Self, Literal, List
from pydantic import BaseModel, Field

from database.UsersDB import UsersDB

class UserDTO(BaseModel):
    id: int
    type: str
    isConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool

    @staticmethod
    async def parse(obj: UsersDB) -> Self:
        return UserDTO(
            id=obj.id,
            type=obj.type,
            isConfirmed=obj.isConfirmed,
            isSupplierStatusConfirmed=obj.isSupplierStatusConfirmed,
            isAdmin=obj.isAdmin
        )

class UserDTOArray(BaseModel):
    usersArray: List[UserDTO]

    @staticmethod
    async def parse(objArr: List[UserDTO]) -> Self:
        return UserDTOArray(
            usersArray=objArr
        )