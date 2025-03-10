#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete, desc
from sqlalchemy import and_

from typing import Self, Dict, List

from .BasicAPI import BasicAPI

# For type annotations
from ..fields.CatalogDB import CatalogDB
DatabaseType = CatalogDB

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
    

    async def get_all_products_time_desc(self, start: int, count: int) -> List[DatabaseType]:
        statement = select(self.base)\
            .order_by(
                    self.base.id.desc()
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out

    async def get_all_products_time_upsc(self, start: int, count: int) -> List[DatabaseType]:
        statement = select(self.base)\
            .order_by(
                    self.base.id
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out

    async def get_my_products_time_desc(self, userId: int, start: int, count: int) -> List[DatabaseType]:
        statement = select(self.base)\
            .where(
                self.base.supplierId == userId,
            ).order_by(
                    self.base.id.desc()
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out

    async def get_my_products_time_upsc(self, userId: int, start: int, count: int) -> List[DatabaseType]:
        statement = select(self.base)\
            .where(
                self.base.supplierId == userId,
            ).order_by(
                    self.base.id
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out

    async def get_product_by_id(self, productId: int) -> DatabaseType:
        statement = select(self.base)\
            .where(
                self.base.id == productId,
            )

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out[0]

    async def search_title_contains_time_upsc(
            self,
            fragment: str,
            start: int,
            count: int
        ) -> DatabaseType:
        statement = select(self.base)\
            .where(
                self.base.title.contains(fragment)
            ).order_by(
                    self.base.id
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out
    
    async def search_title_contains_time_desc(
            self,
            fragment: str,
            start: int,
            count: int
        ) -> DatabaseType:
        statement = select(self.base)\
            .where(
                self.base.title.contains(fragment)
            ).order_by(
                    self.base.id.desc()
            ).offset(start).fetch(count)

        async with self.session() as session:
            out = await session.execute(statement)
        
        return out