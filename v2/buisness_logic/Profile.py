from simple_rpc import GrpcClient, GrpcServer

from commands.UsersCommands import UsersCommands

from output_schemas.ProfileSchemas import *
from input_schemas.Profile import *

UsersClient = GrpcClient(
    port=50501,
    ip="users_controller",
    proto_file_relpath="protos/Users.proto"
)
UsersCommandsManager = UsersCommands(
    client = UsersClient
)
app = GrpcServer()


class ProfileLogic():
    @app.grpc_method()
    async def delete_user(
            self,
            request: UserIdReq
        ) -> EmptyModel:
        await UsersCommandsManager.delete_user_by_id(
            userId=request.userId
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def get_user_info(
            self,
            request: UserIdReq
        ) -> UserSchema:
        resp = await UsersCommandsManager.get_user_by_id(
            userId=request.userId
        )
        return await UserSchema.parse(resp)

app.configure_service(
    cls=ProfileLogic(),
    port=50516
)
app.run()