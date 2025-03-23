import bcrypt

from exceptions.database_exceptions import *
from settings import DBSettings

from database.EmailAuthAPI import EmailAuthAPI
from database.EmailAuthDB import EmailAuthDB

from schemas.RPCScheams import *

from simple_rpc.v2.server import GrpcServerV2

app = GrpcServerV2()

class EmailAuth():
    def __init__(self) -> None:
        self.EmailAuthAPI = EmailAuthAPI(EmailAuthDB, DBSettings.DATABASE_URL)

    @app.grpc_method()
    async def add_auth_method(self, request: AddAuthMethodRequest) -> EmptyResponce:
        password_ = bcrypt.hashpw(request.password.encode(), bcrypt.gensalt()) # encoding password
        await self.EmailAuthAPI.add_auth_method(
            email=request.email,
            password=password_,
            userId=request.userId
        )
        return EmptyResponce()
    
    @app.grpc_method()
    async def remove_auth_method(self, request: RemoveAuthMethodRequest) -> EmptyResponce:
        await self.EmailAuthAPI.remove_auth_method(
            email=request.email
        )
        return EmptyResponce()

    @app.grpc_method()
    async def check_password(self, request: CheckPasswordRequest) -> CheckPasswordResponce:
        user_info = await self.EmailAuthAPI.get_info_by_email(
            email=request.email
        )
        if len(user_info) == 0:
            raise NotExist(
                description="User does not exist"
            )
        return CheckPasswordResponce(
            status=bcrypt.checkpw(
                request.password.encode(),
                user_info[0].password
            )
        )

# SimpleRPC server startup

app.configure_service(
    cls=EmailAuth(),
    port=50502
)
app.run()