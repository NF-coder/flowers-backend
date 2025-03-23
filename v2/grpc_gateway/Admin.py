from schemas.AdminSchemas import *
from typing_extensions import List

from simple_rpc.v2.client import GrpcClientV2

from commands.UsersCommands import UsersCommands

import asyncio

client = GrpcClientV2(
    port=50501
)
commands = UsersCommands(
    client = client
)

class AdminLogic():
    
    @staticmethod
    def __init__(self) -> None:
        pass
    
    async def list_suppliers_requests(
            start: int,
            count: int,
            sort: str
        ) -> List[UserSchema]:
        suppliers_arr = await commands.find_unconfirmed_suppliers()(
            start=start,
            count=count,
            sort=sort
        )
        return [
            await UserSchema.parse(supplier)
            for supplier in suppliers_arr.usersArray
        ]
    
    async def approve_supplier_request(
            id: int
        ) -> None:
        await commands.approve_supplier_request()(
            id=id
        )

async def run():
    print(
        await AdminLogic.list_suppliers_requests(0, 2 , "time_upscending")
    )
    print(
        await AdminLogic.approve_supplier_request(1)
    )

if __name__ == "__main__":
    asyncio.run(
        run()
    )