import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .Basic import Basic
from .ProductAdditionalImages import ProductAdditionalImages
from .Users import Users

from ..backend.api.OrderAPI import OrderAPI
from ..backend.fields.OrderDB import OrderDB

class Order(Basic):
    @classmethod
    async def start(self) -> Self:
        return await self.start_(OrderAPI, OrderDB, SecurityConfig.DATABASE_URL)
    

    async def create_order(self,
        geoId: int,
        userId: int,
        firstName: str,
        secondName: str,
        comment: str,
        phoneNumber: str
    ) -> int:
        
        return await self.api.create_order(
            geoId=geoId,
            userId=userId,
            firstName=firstName,
            secondName=secondName,
            comment=comment,
            phoneNumber=phoneNumber
        )
    
    async def get_by_id(
        self,
        id: int
    ) -> dict:
        return await self.api.get_by_id(
            id=id
        )
    
    async def set_status_by_id(
        self,
        id: int,
        newStatus: str
    ) -> None:
        return await self.api.set_status_by_id(
            id=id,
            newStatus=newStatus
        )
    
    async def cancel_by_id(
        self,
        id: int,
    ) -> None:
        return await self.api.set_cancel_status_by_id(
            id=id,
            newStatus=True
        )

    async def finish_by_id(
        self,
        id: int,
    ) -> None:
        return await self.api.set_finish_status_by_id(
            id=id,
            newStatus=True
        )
    
    async def get_active_by_userId(
        self,
        userId: int,
    ) -> dict:
        return await self.api.get_active_orders_by_userId(
            userId=userId
        )
