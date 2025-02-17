#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

import asyncio
import traceback
import os
from typing import Self, Dict

from .fields import *
from .utils.utils import Middleware_utils

from exceptions.database_exceptions import NoDatabaseConnection

class DB_API:
    @classmethod # Cause I can't use asyncio in __magic__ functions, so...
    async def start(cls, base_fields, base_url) -> Self:
        '''
            Method that starts connection to database
            Args:
                base_fields(`declarative_base()` inheritor?):
                    Schema of databse. Can be found in backend.fields
                base_url(str):
                    Link to database. Starts with (for example): `postgresql+asyncpg://`
            Returns:
                self:
            Raises:
                NoDatabaseConnection: If engine for some reason can't connect to database
        '''
        try:
            self = cls()

            self.base = base_fields
            self.engine = create_async_engine(base_url)

            await self.init_db()

            self.session = sessionmaker(
                bind = self.engine,
                class_ = AsyncSession,
                expire_on_commit = False
            )

        except Exception as exc:
            raise NoDatabaseConnection("Error while connecting to database! [DB_API]")
            #print(f"Error while API init:\n{traceback.format_exc()}\n")

        return self
    
    async def init_db(self): # special function for database startup
        async with self.engine.begin() as conn:
            await conn.run_sync(self.base.metadata.create_all)

class Users_API(DB_API):
    async def register(self, email: str, password: bytes) -> None:
        '''
            Method that registers users.
            Args:
                email(str): user's email
                password(bytes): hashed and salted user's password bytes
            Returns:
                NoneType:
        '''
        async with self.session() as session:
            session.add(self.base(email=email, password=password))
            await session.commit()
    
    async def get_by_email(self, email: str) -> list[Dict]:
        '''
            Method that returns all users with specified email.
            Args:
                email(str): user's email
            Returns:
                list: all user's data
        '''
        async with self.session() as session:
            statement = select(self.base).where(self.base.email == email)
            out = await session.execute(statement)
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )