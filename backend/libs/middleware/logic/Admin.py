from ..main.Users import Users
from .schemas.AdminSchemas import *

from typing_extensions import List

Users = Users()

class AdminLogic():
    @staticmethod
    def __init__(self) -> Self:
        pass
    
    async def list_suppliers_requests(
            start: int,
            count: int,
            sort: str
        ) -> List[UserSchema]:
        suppliers_arr = await Users.find_unconfirmed_suppliers(
            start=start,
            count=count,
            sort=sort
        )
        return [
            await UserSchema.parse(supplier)
            for supplier in suppliers_arr
        ]
    
    async def approve_supplier_request(
            id: int,
            email: str
        ) -> None:
        await Users.confirm_supplier(
            id=id,
            email=email
        )