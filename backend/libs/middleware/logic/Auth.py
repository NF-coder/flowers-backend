from ..main.Users import Users
from .schemas.AuthSchemas import UserSchema

from typing_extensions import List, Self
from exceptions import BasicException

Users = Users()

class AuthLogic():
    @staticmethod
    def __init__(self) -> Self:
        pass
    
    async def sign_in(
            email: str,
            password: str
        ) -> UserSchema:
        isCrrectPassword = await Users.check_password_by_email(
            email=email,
            password=password
        )
        if not isCrrectPassword:
            raise BasicException(
                code=400,
                description="Incorrect password"
            )
        result = Users.get_info_by_email(
            email=email
        )
        return await UserSchema.parse(result)
    
    async def register(
            email: str,
            password: str,
            type: str
        ) -> UserSchema:
        await Users.register(
            email=email,
            password=password, 
            type=type
        )
        new_user_data = await Users.get_info_by_email(
            email=email
        )
        return await UserSchema.parse(new_user_data)
    
    async def confirmEmail(
            id: int
        ) -> UserSchema:
        await Users.confirm_email(id = id)
        new_user_data = await Users.get_info_by_id(
            id=id
        )
        return await UserSchema.parse(new_user_data)
    
    async def delete_user(
            email: str
        ) -> None:
        await Users.delete_user_by_email(
            email=email
        )  