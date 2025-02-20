# Submodules import
from .backend.api import *
from .backend.fields import *

import traceback
import asyncio
import bcrypt

from typing import Self

from exceptions.database_exceptions import *
from settings import SecuritySettings

class Base:
    @classmethod
    async def start_(cls, api: DB_API, base_fields: Users_DB, base_url: str) -> Self:
        '''
            Method that starts connection to database
            Args:
                api(`DB_API` class inheritor):
                    Low-level API of database. Can be found in backemd.api
                base_fields(`declarative_base()` inheritor):
                    Schema of databse. Can be found in backend.fields
                base_url(str):
                    Link to database. Starts with (for example): `postgresql+asyncpg://`
            Returns:
                self:
        '''

        self = cls()
        self.api = await api.start(base_fields, base_url)

        return self

class Users(Base):
    @classmethod
    async def start(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `Users` object
        '''
        return await self.start_(Users_API, Users_DB, SecuritySettings.DATABASE_URL)
    
    async def is_email_registered(self, email: str) -> bool:
        '''
            Method that checks if login is in database
            Args:
                login(str): login (email in our case)
            Returns:
                bool: True if already in database
        '''
        return len(await self.api.get_by_email(email)) == 1
    
    async def is_id_registered(self, id: int) -> bool:
        '''
            Method that checks if id is in database
            Args:
                id(int): id
            Returns:
                bool: True if already in database
        '''
        return len(await self.api.get_by_id(id)) == 1
    
    async def register(self, email: str, password: str, type: str) -> None:
        '''
            Method that register new user.
            Args:
                email(str): user's email
                password(str): user's password
                type(str): user's account type
            Returns:
                NoneType:
            Raises:
                NotUnique: If email is not unique
        '''
        if await self.is_email_registered(email):
            raise NotUnique(
                description="Email is not unique"
            )

        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) # encoding password
        await self.api.register(
            email=email,
            password=password,
            type=type
        )
    
    async def get_by_email(self, email: str) -> list:
        '''
            Method that gets user from database.
            Args:
                email(str): user's email (in our case)
            Returns:
                NoneType:
            Raises:
                NotExist: if no users with specified email
        '''
        if not (await self.is_email_registered(email)):
            raise NotExist(description = "User does not exist")
        
        return (await self.api.get_by_email(email))[0]
    
    async def get_by_id(self, id: int) -> list:
        '''
            Method that gets user from database.
            Args:
                id(int): user's id
            Returns:
                NoneType:
            Raises:
                NotExist: if no users with specified id
        '''
        if not (await self.is_id_registered(id)):
            raise NotExist(description = "User does not exist")
        
        return (await self.api.get_by_id(id))[0]

    async def check_password_by_email(self, email: str, password: str) -> bool:
        '''
            Method that gets user from database by email.
            Args:
                email(str): user's email (in our case)
            Returns:
                NoneType:
            Raises:
                NotExist: if no users with specified email
        '''
        if not (await self.is_email_registered(email)):
            raise NotExist(
                description="User does not exist"
            )
        
        return bcrypt.checkpw(password.encode(), (await self.api.get_by_email(email))[0]["password"])
    
    async def set_email_confirmation_status(self, id: int, status: bool = True) -> None:
        '''
            Method that sets user's email confirmation status
            Args:
                id(int): User's id
                status(bool?): New email confirmation status. Default `True`
            Returns:
                NoneType:
        '''
        await self.api.set_email_confirmation_status_by_id(
            id=id,
            status=status
        )