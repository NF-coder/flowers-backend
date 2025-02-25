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
        ) -> int:

        statement = select(self.base).where(self.base.id == id)
        async with self.session() as session:
            out = await session.execute(statement)
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )

