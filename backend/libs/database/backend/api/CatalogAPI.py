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

class CatalogAPI(BasicAPI):
    async def create_product(
            self,
            title: str,
            titleImageUrl: str,
            costNum: int,
            description: str,
            authorId: int,
        ) -> int:
        '''
            Method that creates new product card.
            Args:
                title(str): product title
                titleImageUrl(bytes): product title image
                costNum(int): cost in RUB
                description(str): product description
                authorId(int): id of user, that created card
            Returns:
                int: id of created product
        '''
        statement = self.base(
            title=title,
            titleImage=titleImageUrl,
            cost=costNum,
            description=description,
            supplierId=authorId
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
        return statement.id
    
    async def get_my_products_time_desc(self, userId: int, start: int, count: int) -> int:
        statement = select(self.base)\
            .where(
                self.supplierId.userId == userId,
            ).order_by(
                    self.base.id.desc()
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )

    async def get_my_products_time_upsc(self, userId: int, start: int, count: int) -> int:
        statement = select(self.base)\
            .where(
                self.base.supplierId == userId,
            ).order_by(
                    self.base.id
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )