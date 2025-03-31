from exceptions.database_exceptions import *
from settings import DBSettings

from database.TgIdAuthAPI import TgIdAuthAPI
from database.TgIdAuthDB import TgIdAuthDB

from simple_rpc import GrpcServer

from schemas.RPCSchemas import *

app = GrpcServer()

class TgIdAuth():
    def __init__(self) -> None:
        self.TgIdAuthAPI = TgIdAuthAPI(TgIdAuthDB, DBSettings.DATABASE_URL)

    
    @app.grpc_method()
    async def add_auth_method(self, request: AddAuthMethodReq) -> EmptyModel:
        await self.TgIdAuthAPI.add_auth_method(
            tgId=request.tgId,
            userId=request.userId
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def remove_auth_method(self, request: TgIdReq) -> EmptyModel:
        await self.TgIdAuthAPI.remove_auth_method(
            tgId=request.tgId
        )
        return EmptyModel()
    
    @app.grpc_method()
    async def get_userId_by_tg_id(self, request: TgIdReq) -> UserIdResp:
        user_info = await self.TgIdAuthAPI.get_user_by_tgId(
            tgId=request.tgId
        )
        if len(user_info) == 0:
            raise NotExist(
                description="User does not exist"
            )
        return UserIdResp(
            userId=user_info[0].userId
        )

# SimpleRPC server startup

app.configure_service(
    cls=TgIdAuth(),
    port=50507
)
app.run()