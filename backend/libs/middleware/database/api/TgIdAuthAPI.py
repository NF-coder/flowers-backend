#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from typing import Self, Dict, List
from typing_extensions import Annotated

from .BasicAPI import BasicAPI

from exceptions.database_exceptions import NoDatabaseConnection

# For type annotations
from ..fields.TgIdAuthDB import TgIdAuthDB
DatabaseType = TgIdAuthDB

class TgIdAuthAPI(BasicAPI):
    async def add_auth_method(self, tgId: int, userId: int) -> None:
        statement = self.base(
            tgId = tgId,
            userId = userId
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
        
    async def remove_auth_method(self, tgId: int) -> None:
        statement = delete(self.base).where(self.base.tgId == tgId)

        async with self.session() as session:
            session.add(statement)
            await session.commit()