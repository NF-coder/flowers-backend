from simple_rpc import GrpcClient, GrpcServer

from commands.UsersCommands import UsersCommands

from output_schemas.AdminSchemas import *
from input_schemas.Admin import *

import asyncio

client = GrpcClient(
    port=50501,
    ip="users_controller",
    proto_file_relpath="protos/Users.proto"
)
commands = UsersCommands(
    client = client
)

app = GrpcServer()

class AdminLogic():
    def __init__(self) -> None:
        pass
    
    @app.grpc_method()
    async def list_suppliers_requests(
            self,
            request: ListSuppliersRequestsReq
        ) -> UserSchemasArray:
        suppliers_arr = await commands.find_unconfirmed_suppliers(
            start=request.start,
            count=request.count,
            sort=request.sort
        )
        return UserSchemasArray(
            UserSchemasArray = [
                await UserSchema.parse(supplier)
                for supplier in suppliers_arr.usersArray
            ]
        )
    
    @app.grpc_method()
    async def approve_supplier_request(
            self,
            request: ApproveSupplierRequestReq
        ) -> EmptyModel:
        await commands.approve_supplier_request(
            id=request.id
        )
        return EmptyModel()


app.configure_service(
    cls=AdminLogic(),
    port=50511
)
app.run()
