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

class OrderAPI(BasicAPI):
    async def create_order(
            self,

            geoId: int,
            userId: int,
            productId: int,

            firstName: str,
            secondName: str,
            comment: str,
            phoneNumber: str
        ) -> int:

        statement = self.base(
            costumerFirstName=firstName,
            costumerSecondName=secondName,
            comment=comment,
            phoneNumber=phoneNumber,
            geoId=geoId,
            userId=userId,
            productId=productId
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
        return statement.id
    

    async def get_by_id(
            self,
            id: int
        ) -> dict:

        statement = select(self.base).where(self.base.id == id)
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

    async def set_status_by_id(
            self,
            id: int,
            newStatus: str
        ) -> None:

        statement = update(self.base).where(self.base.id == id).values(
            orderStatus=newStatus
        )

        async with self.session() as session:
            await session.execute(statement)
            await session.commit()

    async def set_cancel_status_by_id(
            self,
            id: int,
            newStatus: bool
        ) -> None:

        statement = update(self.base).where(self.base.id == id).values(
            isCanceled=newStatus
        )

        async with self.session() as session:
            await session.execute(statement)
            await session.commit()
    
    async def set_finish_status_by_id(
            self,
            id: int,
            newStatus: bool
        ) -> None:

        statement = update(self.base).where(self.base.id == id).values(
            isFinished=newStatus
        )

        async with self.session() as session:
            await session.execute(statement)
            await session.commit()

    async def get_all_orders_by_userId(
            self,
            userId: int,
            start: int,
            count: int
        ) -> None:

        statement = select(self.base).where(self.base.userId == userId)

        async with self.session() as session:
            out = await session.execute(statement)

        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
    
    async def get_active_orders_by_userId(
            self,
            userId: int,
        ) -> None:

        statement = select(self.base).where(
            and_(
                self.base.userId == userId,
                self.base.isCanceled == False,
                self.base.isFinished == False
                )
            )

        async with self.session() as session:
            out = await session.execute(statement)

        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
    
    async def get_all_active_orders(
            self
        ) -> None:

        statement = select(self.base).where(
            and_(
                self.base.isCanceled == False,
                self.base.isFinished == False
                )
            )

        async with self.session() as session:
            out = await session.execute(statement)

        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
    
    async def get_all_active_orders_with_productId(
            self,
            productId: int
        ) -> dict:

        statement = select(self.base).where(
            and_(
                self.base.isCanceled == False,
                self.base.isFinished == False,
                self.base.productId == productId
                )
            )

        async with self.session() as session:
            out = await session.execute(statement)

        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )