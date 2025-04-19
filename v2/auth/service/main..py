import redis
from simple_rpc import GrpcServer
from tokens.main import Tokens

app = GrpcServer()

class AuthLogic():
    @app.grpc_method()
    async def create_token(basicToken: str):
        userInfo = await Tokens.decode_acess_token(
            token = basicToken
        )
        
        return await Tokens.get_acess_token()

    @app.grpc_method()
    async def check_token():
        pass

    @app.grpc_method()
    async def deactivate_token():
        pass