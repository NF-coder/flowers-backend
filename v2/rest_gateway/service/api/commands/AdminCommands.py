from .schemas.AdminCommandsScemas import *

from simple_rpc import GrpcClient

class AdminCommands:
    def __init__(self, client: GrpcClient) -> None:
        self.list_suppliers_requests__ = client.configure_command(
            functionName="list_suppliers_requests",
            className="AdminLogic"
        )
        self.approve_supplier_request__ = client.configure_command(
            functionName="approve_supplier_request",
            className="AdminLogic"
        )
    
    async def list_suppliers_requests(self, start: int, count: int, sort: str) -> list[UserSchema]:
        return [
            UserSchema(
                userId=user.userId,
                type=user.type,
                isConfirmed=user.isConfirmed,
                isSupplierStatusConfirmed=user.isSupplierStatusConfirmed,
                isAdmin=user.isAdmin
            )
            for user in await self.list_suppliers_requests__(
                start = start,
                count = count,
                sort = sort,
            )
        ]
    
    async def approve_supplier_request(self, userId: int) -> None:
        await self.approve_supplier_request__(
            id = userId
        )
    