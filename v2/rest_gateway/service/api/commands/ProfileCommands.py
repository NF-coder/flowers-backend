from .schemas.CatalogCommandsSchemas import *

from simple_rpc import GrpcClient

from .schemas.ProfileCommandsSchems import *

class ProfileCommands:
    def __init__(self, client: GrpcClient) -> None:
        self.delete_user__ = client.configure_command(
            functionName="delete_user",
            className="ProfileLogic"
        )
        self.get_user_info__ = client.configure_command(
            functionName="get_user_info",
            className="ProfileLogic"
        )

    async def delete_user(self, userId: int) -> None:
        await self.delete_user__(
            userId=userId
        )
    
    async def get_user_info(self, userId: int) -> UserSchema:
        resp = await self.get_user_info__(
            userId=userId
        )
        return UserSchema.model_validate(
            resp,
            from_attributes=True
        )