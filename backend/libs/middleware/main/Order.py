import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .ProductAdditionalImages import ProductAdditionalImages
from .Users import Users

from ..database.api.OrderAPI import OrderAPI
from ..database.fields.OrderDB import OrderDB

from .schemas.OrderSchemas import OrderDTO

class Order():
    def __init__(self) -> Self:
        self.OrderAPI = OrderAPI(OrderDB, SecurityConfig.DATABASE_URL)

    async def create_order(self,
        geoId: int,
        userId: int,
        productId:int,
        firstName: str,
        secondName: str,
        comment: str,
        phoneNumber: str,
    ) -> int:
        
        return await self.OrderAPI.create_order(
            geoId=geoId,
            userId=userId,
            firstName=firstName,
            secondName=secondName,
            comment=comment,
            phoneNumber=phoneNumber,
            productId=productId
        )
    
    async def get_by_id(
        self,
        id: int
    ) -> OrderDTO:
        result = await self.OrderAPI.get_by_id(
            id=id
        )
        return await OrderDTO.parse(result)
    
    async def get_by_productId(
        self,
        productId: int
    ) -> List[OrderDTO]:
        result = await self.OrderAPI.get_by_productId(
            productId=productId
        )
        return [
            await OrderDTO.parse(order)
            for order in result
        ]
    
    async def set_status_by_id(
        self,
        id: int,
        newStatus: str
    ) -> None:
        await self.OrderAPI.set_status_by_id(
            id=id,
            newStatus=newStatus
        )
    
    async def cancel_by_id(
        self,
        id: int,
    ) -> None:
        await self.OrderAPI.set_cancel_status_by_id(
            id=id,
            newStatus=True
        )

    async def finish_by_id(
        self,
        id: int,
    ) -> None:
        await self.OrderAPI.set_finish_status_by_id(
            id=id,
            newStatus=True
        )
    
    async def get_active_by_userId(
        self,
        userId: int,
    ) -> List[OrderDTO]:
        result = await self.OrderAPI.get_active_orders_by_userId(
            userId=userId
        )
        return [
            await OrderDTO.parse(order)
            for order in result
        ]
    
    
    async def get_all_active(
        self
    ) -> List[OrderDTO]:
        result = await self.OrderAPI.get_all_active_orders()
        return[
            await OrderDTO.parse(order)
            for order in result
        ]
    
    

    async def get_active_with_productId(
        self,
        productId: int
    ) -> List[OrderDTO]:
        result = await self.OrderAPI.get_all_active_orders_with_productId(
            productId = productId
        )
        return[
            await OrderDTO.parse(order)
            for order in result
        ]