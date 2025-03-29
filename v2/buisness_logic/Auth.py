from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient, GrpcServer

from commands.UsersCommands import UsersCommands
from commands.AuthCommands import AuthCommands

from output_schemas.AuthSchemas import *
from input_schemas.Auth import *

import asyncio

UsersClient = GrpcClient(
    port=50501,
    proto_file_relpath="protos/Users.proto"
)
AuthClient = GrpcClient(
    port=50502,
    proto_file_relpath="protos/EmailAuth.proto"
)
UsersCommandsManager = UsersCommands(
    client = UsersClient
)
EmailAuthCommandsManager = AuthCommands(
    client = AuthClient
)
app = GrpcServer()

class AuthLogic():
    def __init__(self) -> None:
        pass
    
    @app.grpc_method()
    async def sign_in_by_email(
            self,
            request: SignInByEmailReq
        ) -> UserSchema:
        passwordCheckResponce = await EmailAuthCommandsManager.check_password_by_email(
            email=request.email,
            password=request.password
        )
        if not passwordCheckResponce.status:
            raise BasicException(
                code=400,
                description="Incorrect password"
            )
        result = await UsersCommandsManager.get_user_by_id(
            userId=passwordCheckResponce.userId
        )
        return await UserSchema.parse(result)
    
    @app.grpc_method()
    async def register_by_email(
            self,
            request: RegisterByEmailReq
        ) -> UserSchema:
        new_user = await UsersCommandsManager.add_new_user(
            type=request.type
        )
        await EmailAuthCommandsManager.add_auth_by_email(
            email=request.email,
            password=request.password,
            userId=new_user.userId    
        )
        new_user_data = await UsersCommandsManager.get_user_by_id(
            userId=new_user.userId   
        )
        return await UserSchema.parse(new_user_data)
    
    async def sign_in_by_tg_id(
            self,
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
    
    async def register_by_tg_id(
            self,
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
            self,
            id: int
        ) -> UserSchema:
        await Users.confirm_email(id = id)
        new_user_data = await Users.get_info_by_id(
            id=id
        )
        return await UserSchema.parse(new_user_data)
    
    async def delete_user(
            self,
            email: str
        ) -> None:
        await Users.delete_user_by_email(
            email=email
        )

app.configure_service(
    cls=AuthLogic(),
    port=50512
)
app.run()