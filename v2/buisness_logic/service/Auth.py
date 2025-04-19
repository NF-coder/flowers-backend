from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient, GrpcServer

from commands.UsersCommands import UsersCommands
from commands.AuthCommands import AuthCommands
from commands.TgIdAuthCommands import TgIdAuthCommands

from output_schemas.AuthSchemas import *
from input_schemas.Auth import *

import asyncio

UsersClient = GrpcClient(
    port=50501,
    ip="users_controller",
    proto_file_relpath="protos/Users.proto"
)
AuthClient = GrpcClient(
    port=50502,
    ip="email_auth_controller",
    proto_file_relpath="protos/EmailAuth.proto"
)
TgIdAuth = GrpcClient(
    port=50507,
    ip="tg_id_auth_controller",
    proto_file_relpath="protos/TgIdAuth.proto"
)
UsersCommandsManager = UsersCommands(
    client = UsersClient
)
EmailAuthCommandsManager = AuthCommands(
    client = AuthClient
)
TgIdAuthCommandsManager = TgIdAuthCommands(
    client = TgIdAuth
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
    
    @app.grpc_method()
    async def sign_in_by_tg_id(
            self,
            request: TgIdModel
        ) -> UserSchema:
        userId = (await TgIdAuthCommandsManager.get_userId_by_tgId(
            tgId=request.tgId
        )).userId
        result = await UsersCommandsManager.get_user_by_id(
            userId=userId
        )
        return await UserSchema.parse(result)
    
    @app.grpc_method()
    async def register_by_tg_id(
            self,
            request: RegisterByTgId
        ) -> UserSchema:
        new_user = await UsersCommandsManager.add_new_user(
            type=request.type
        )
        await TgIdAuthCommandsManager.add_auth_method(
            tgId=request.tgId,
            userId=new_user.userId    
        )
        new_user_data = await UsersCommandsManager.get_user_by_id(
            userId=new_user.userId   
        )
        return await UserSchema.parse(new_user_data)
    

app.configure_service(
    cls=AuthLogic(),
    port=50512
)
app.run()