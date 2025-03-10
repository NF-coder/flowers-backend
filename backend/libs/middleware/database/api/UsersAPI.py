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
from ..fields.UsersDB import UsersDB
DatabaseType = UsersDB

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
    
    async def get_by_email(self, email: str) -> DatabaseType:
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
        return out[0]
    
    async def get_by_id(self, id: int) -> DatabaseType:
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
        return out[0]
    
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
    
    async def find_suppliers_with_status_upscending(
            self,
            start: int,
            count: int,
            confrmationStatus: bool
        ) -> List[DatabaseType]:
        '''
            Method that finds all suppliers with specified status
            Sorted from lower to gater id
            Args:
                count (int):
                    How many users may database find.
                    Number of returned users be smaller, then specified lenght
                start (int):
                    Offset of firs user in list. Can affect result array lenght
                confrmationStatus(bool): 
                    Supplier status
            Returns:
                NoneType:
        '''
        statement = select(self.base.email, self.base.id)\
            .where(
                and_(
                    self.base.type == "supplier" ,
                    self.base.isSupplierStatusConfirmed == False
                )
            )\
            .order_by(
                self.base.id
            )\
            .offset(start).fetch(count)
        
        async with self.session() as session:
            out = await session.execute(statement)
        
        return out
    
    async def find_suppliers_with_status_descending(
            self,
            start: int,
            count: int,
            confrmationStatus: bool
        ) -> list[DatabaseType]:
        '''
            Method that finds all suppliers with specified status.
            Sorted from grater to lower id
            Args:
                count (int):
                    How many users may database find.
                    Number of returned users be smaller, then specified lenght
                start (int):
                    Offset of firs user in list. Can affect result array lenght
                confrmationStatus(bool): supplier status
            Returns:
                NoneType:
        '''
        statement = select(self.base.email, self.base.id)\
            .where(
                and_(
                    self.base.type == "supplier" ,
                    self.base.isSupplierStatusConfirmed == False
                )
            )\
            .order_by(
                self.base.id.desc()
            )\
            .offset(start).fetch(count)
        
        async with self.session() as session:
            out = await session.execute(statement)
        
        return out
    
    async def set_admin_status_by_email(self, email: str, status: bool) -> None:
        '''
            Method that makes user admin
            Args:
                email(str): user's email
                status(bool): new user admin status
            Returns:
                NoneType:
        '''
        statement = update(self.base).where(self.base.email == email).values(
            isAdmin=status
        )
        async with self.session() as session:
            await session.execute(statement)
            await session.commit()

    async def set_supplier_status_by_email(self, email: str, status: bool) -> None:
        '''
            Method that sets/unsets isSupplierStatusConfirmed for the specified user 
            Args:
                email(str): user's email
                status(bool): new user admin status
            Returns:
                NoneType:
        '''
        statement = update(self.base).where(self.base.email == email).values(
            isSupplierStatusConfirmed=status
        )
        async with self.session() as session:
            await session.execute(statement)
            await session.commit()
    
    async def set_supplier_status_by_id(self, id: int, status: bool) -> None:
        '''
            Method that sets/unsets isSupplierStatusConfirmed for the specified user 
            Args:
                id(int): user's id
                status(bool): new user admin status
            Returns:
                NoneType:
        '''
        statement = update(self.base).where(self.base.id == id).values(
            isSupplierStatusConfirmed=status
        )
        async with self.session() as session:
            await session.execute(statement)
            await session.commit()