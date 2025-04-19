from .schemas.UsersModels import *

from simple_rpc import GrpcClient

class UsersCommands():
    def __init__(self, client: GrpcClient) -> None:
        self.find_unconfirmed_suppliers__ = client.configure_command(
            functionName="find_unconfirmed_suppliers",
            className="Users"
        )
        self.approve_supplier_request__  = client.configure_command(
            functionName="confirm_supplier_by_id",
            className="Users"
        )
        self.add_new_user__ = client.configure_command(
            functionName="add_new_user",
            className="Users"
        )
        self.get_user_by_id__ = client.configure_command(
            functionName="get_info_by_id",
            className="Users"
        )
        self.delete_user_by_id__ = client.configure_command(
            functionName="delete_user_by_id",
            className="Users"
        )
    
    async def find_unconfirmed_suppliers(self, start: int, count: int, sort: str) -> UsersArray:
        return UsersArray.model_validate(
            await self.find_unconfirmed_suppliers__(
                start=start,
                count=count,
                sort=sort
            ),
            from_attributes=True
        )
    
    async def approve_supplier_request(self, id: int) -> None:
        await self.approve_supplier_request__(
            userId=id
        )

    async def add_new_user(self, type: str) -> UserId:
        return UserId.model_validate(
            await self.add_new_user__(
                type=type
            ),
            from_attributes=True
        )

    async def get_user_by_id(self, userId: int) -> User:
        resp = await self.get_user_by_id__(
            userId = userId
        )
        return User.model_validate(
            resp,
            from_attributes=True
        )
    
    async def delete_user_by_id(self, userId: int) -> None:
        await self.delete_user_by_id__(
            userId = userId
        )