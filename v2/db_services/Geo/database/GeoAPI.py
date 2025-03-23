#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from typing import Self, Dict, List

from .BasicAPI import BasicAPI

from exceptions.database_exceptions import NoDatabaseConnection

# For type annotations
from .GeoDB import GeoDB
DatabaseType = GeoDB

class GeoAPI(BasicAPI):
    async def add_geo(
            self,

            country: str,
            city: str,
            street: str,
            building: str,
            flat: str,

            userId: int
        ) -> int:

        statement = self.base(
            userId=userId,
            country=country,
            city=city,
            street=street,
            building=building,
            flat=flat
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
        return statement.id
    

    async def get_by_id(
            self,
            id: int
        ) -> DatabaseType:

        statement = select(self.base).where(self.base.id == id)
        async with self.session() as session:
            out = await session.execute(statement)
        return out[0]

