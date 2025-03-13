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
from ..fields.EmailAuthDB import EmailAuthDB
DatabaseType = EmailAuthDB

class EmailAuthAPI(BasicAPI):
    async def add_auth_method(self, email: str, password: bytes, userId: int) -> None:
        statement = self.base(
            email=email,
            password=password,
            userId=userId
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()

    async def remove_auth_method(self, email: str) -> None:
        statement = delete(self.base).where(self.base.email == email)

        async with self.session() as session:
            session.add(statement)
            await session.commit()
    
    async def check_password_by_email(self, email: str) -> None:
        statement = delete(self.base).where(self.base.email == email)

        async with self.session() as session:
            session.add(statement)
            await session.commit()