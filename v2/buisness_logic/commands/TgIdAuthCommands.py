
from simple_rpc import GrpcClient

from .schemas.TgIdAuthModels import *

class TgIdAuthCommands():
    def __init__(self, client: GrpcClient) -> None:
        self.add_auth_method__ = client.configure_command(
            functionName="add_auth_method",
            className="TgIdAuth"
        )
        self.remove_auth_method__ = client.configure_command(
            functionName="remove_auth_method",
            className="TgIdAuth"
        )
        self.get_userId_by_tg_id__ = client.configure_command(
            functionName="get_userId_by_tg_id",
            className="TgIdAuth"
        )

    async def add_auth_method(self, tgId: int, userId: int) -> None:
        await self.add_auth_method__(
            tgId=tgId,
            userId=userId
        )

    async def remove_auth_method(self, tgId: int) -> None:
        await self.remove_auth_method__(
            tgId=tgId
        )

    async def get_userId_by_tgId(self, tgId: int) -> UserIdModel:
        return UserIdModel(
            userId = await self.get_userId_by_tg_id__(
                tgId=tgId
            )
        )