import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .Basic import Basic
from .ProductAdditionalImages import ProductAdditionalImages
from .Users import Users

from ..backend.api.OrderProductsAPI import OrderProductsAPI
from ..backend.fields.OrderProductsDB import OrderProductsDB

class OrderProducts(Basic):
    @classmethod
    async def start(self) -> Self:
        return await self.start_(OrderProductsAPI, OrderProductsDB, SecurityConfig.DATABASE_URL)
    

    async def add_products(
            self,
            userId: int,
            orderId: int,
            productIds: List[int],
        ) -> List[int]:
        out = []
        for id in productIds:
            out.append(
                await self.api.add_product(
                    userId=userId,
                    orderId=orderId,
                    productId=id
                )
            )
        return out
    
    async def get_by_orderId(
            self,
            orderId: int,
        ) -> List[dict]:
        return await self.api.get_by_orderId(
                orderId=orderId
            )

    async def get_by_productId(
            self,
            productId: int,
        ) -> List[dict]:
        return await self.api.get_by_productId(
                productId=productId
            )

