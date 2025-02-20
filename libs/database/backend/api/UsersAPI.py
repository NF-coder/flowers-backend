#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete
from sqlalchemy.orm import sessionmaker

import asyncio
import traceback
import os
from typing import Self, Dict

from ..utils.utils import Middleware_utils
from .BasicAPI import BasicAPI

from exceptions.database_exceptions import NoDatabaseConnection

class UsersAPI(BasicAPI):
    async def register(self, email: str, password: bytes, type: str) -> None:
        '''
            Method that registers users.
            Args:
                email(str): user's email
                password(bytes): hashed and salted user's password bytes
                type(str): user's account type
            Returns:
                NoneType:
        '''
        statement = self.base(
            email=email,
            password=password,
            type=type,
            isEmailConfirmed=False,
            isSupplierStatusConfirmed=False
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
    
    async def get_by_email(self, email: str) -> list[Dict]:
        '''
            Method that returns all users with specified email.
            Args:
                email(str): user's email
            Returns:
                list: all user's data
        '''
        statement = select(self.base).where(self.base.email == email)
        async with self.session() as session:
            out = await session.execute(statement)
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
    
    async def get_by_id(self, id: int) -> list[Dict]:
        '''
            Method that returns all user with specified id.
            Args:
                id(str): user's id
            Returns:
                list: all user's data
        '''
        statement = select(self.base).where(self.base.id == id)
        async with self.session() as session:
            out = await session.execute(statement)
        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__
                    )
    
    async def set_email_confirmation_status_by_id(self, id: int, status: bool) -> None:
        '''
            Method that returns all user with specified id.
            Args:
                id(int): User's id
                status(bool): New email confirmation status 
            Returns:
                NoneType:
        '''
        statement = update(self.base).where(self.base.id == id).values(
            isEmailConfirmed=status
        )
        async with self.session() as session:
            await session.execute(statement)
            await session.commit()
    
    async def delete_by_id(self, id: int) -> None:
        '''
            Method that deleted user with specified id.
            Args:
                id(int): User's id
            Returns:
                NoneType:
        '''
        statement = delete(self.base).where(self.base.id == id)
        async with self.session() as session:
            await session.execute(statement)
            await session.commit()
    
    async def delete_by_email(self, email: str) -> None:
        '''
            Method that deleted user with specified id.
            Args:
                email(str): User's email
            Returns:
                NoneType:
        '''
        statement = delete(self.base).where(self.base.email == email)
        async with self.session() as session:
            await session.execute(statement)
            await session.commit()
    