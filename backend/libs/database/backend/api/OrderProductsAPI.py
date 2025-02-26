#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

import asyncio
import traceback
import os
from typing import Self, Dict, List

from ..utils.utils import Middleware_utils
from .BasicAPI import BasicAPI

from exceptions.database_exceptions import NoDatabaseConnection

class OrderProductsAPI(BasicAPI):
    async def add_product(
            self,
            
            userId: int,
            orderId: int,
            productId: int,
        ) -> int:


        statement = self.base(
            userId=userId,
            orderId=orderId,
            productId=productId
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
        return statement.id
    
    async def get_by_orderId(
            self,
            orderId: int
        ) -> dict:

        statement = select(self.base).where(self.base.orderId == orderId)
        async with self.session() as session:
            out = await session.execute(statement)
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
    async def get_by_productId(
            self,
            productId: int
        ) -> dict:

        statement = select(self.base).where(self.base.productId == productId)
        async with self.session() as session:
            out = await session.execute(statement)
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
