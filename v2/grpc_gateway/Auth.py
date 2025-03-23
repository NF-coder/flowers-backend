from schemas.AuthSchemas import UserSchema

from typing_extensions import List, Self
from exceptions.basic_exception import BasicException

from simple_rpc.v2.client import GrpcClientV2

from commands.UsersCommands import UsersCommands
from commands.AuthCommands import AuthCommands

import asyncio
import pathlib

UsersClient = GrpcClientV2(
    port=50501,
    proto_dir_relpath=pathlib.Path("proto_tmp/auth/users")
)
AuthClient = GrpcClientV2(
    port=50502,
    proto_dir_relpath=pathlib.Path("proto_tmp/auth/emailAuth")
)
UsersCommandsManager = UsersCommands(
    client = UsersClient
)
EmailAuthCommandsManager = AuthCommands(
    client = AuthClient
)

class AuthLogic():
    @staticmethod
    def __init__(self) -> None:
        pass
    
    async def sign_in_by_email(
            email: str,
            password: str
        ) -> UserSchema:
        isCrrectPassword = await Users.check_password(
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
    
    async def sign_in_by_tg_id(
            tgId: int
        ) -> UserSchema:
        isCrrectPassword = await TgIdAuth.check_password_by_email(
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
    
    
    async def register_by_email(
            email: str,
            password: str,
            type: str
        ) -> UserSchema:
        new_user = await UsersCommandsManager.add_new_user()(
            type=type
        )
        await EmailAuthCommandsManager.add_auth_by_email()(
            email=email,
            password=password,
            userId=new_user.id    
        )
        new_user_data = await UsersCommandsManager.get_user_by_id()(
            id=new_user.id   
        )
        return await UserSchema.parse(new_user_data)
    
    async def register_by_tg_id(
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

async def run():
    print(
        await AuthLogic.register_by_email("ex1@eample.com", "12345678", "costumer")
    )

if __name__ == "__main__":
    asyncio.run(
        run()
    )