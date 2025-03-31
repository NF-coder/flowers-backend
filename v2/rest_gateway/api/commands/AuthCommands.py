from .schemas.AuthCommandsSchemas import *

from simple_rpc import GrpcClient

class AuthCommands:
    def __init__(self, client: GrpcClient) -> None:
        self.sign_in_by_email__ = client.configure_command(
            functionName="sign_in_by_email",
            className="AuthLogic"
        )
        self.register_by_email__ = client.configure_command(
            functionName="register_by_email",
            className="AuthLogic"
        )
        self.sign_in_by_tg_id__ = client.configure_command(
            functionName="sign_in_by_tg_id",
            className="AuthLogic"
        )
        self.register_by_tg_id__ = client.configure_command(
            functionName="register_by_tg_id",
            className="AuthLogic"
        )
    
    async def sign_in_by_email(self, email: str, password: str) -> UserSchema:
        responce =  await self.sign_in_by_email__(
            email = email,
            password = password
        )
        return UserSchema(
            userId=responce.userId,
            type=responce.type,
            isConfirmed=responce.isConfirmed,
            isSupplierStatusConfirmed=responce.isSupplierStatusConfirmed,
            isAdmin=responce.isAdmin
        )

    async def register_by_email(self, email: str, password: str, type: str) -> UserSchema:
        responce = await self.register_by_email__(
            email = email,
            password = password,
            type = type
        )
        return UserSchema(
            userId=responce.userId,
            type=responce.type,
            isConfirmed=responce.isConfirmed,
            isSupplierStatusConfirmed=responce.isSupplierStatusConfirmed,
            isAdmin=responce.isAdmin
        )
    
    async def sign_in_by_tgId(self, tgId: int) -> UserSchema:
        responce = await self.sign_in_by_tg_id__(
            tgId=tgId
        )
        return UserSchema(
            userId=responce.userId,
            type=responce.type,
            isConfirmed=responce.isConfirmed,
            isSupplierStatusConfirmed=responce.isSupplierStatusConfirmed,
            isAdmin=responce.isAdmin
        )
    
    async def register_by_tgId(self, tgId: int, type: str) -> UserSchema:
        responce = await self.register_by_tg_id__(
            tgId = tgId,
            type = type
        )
        return UserSchema(
            userId=responce.userId,
            type=responce.type,
            isConfirmed=responce.isConfirmed,
            isSupplierStatusConfirmed=responce.isSupplierStatusConfirmed,
            isAdmin=responce.isAdmin
        )