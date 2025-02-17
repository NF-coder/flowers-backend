# Submodules import
from .backend.api import *
from .backend.fields import *

import traceback
import asyncio
import bcrypt

from typing import Self

from exceptions.database_exceptions import *

class Base:
    @classmethod
    async def start_(cls, api: DB_API, base_fields: Users_DB, base_url: str) -> Self:
        '''
            Method that starts connection to database
            Args:
                api(`DB_API` class inheritor):
                    Low-level API of database. Can be found in backemd.api
                base_fields(`declarative_base()` inheritor?):
                    Schema of databse. Can be found in backend.fields
                base_url(str):
                    Link to database. Starts with (for example): `postgresql+asyncpg://`
            Returns:
                self:
            Raises:
                NoDatabaseConnection: If engine for some reason can't connect to database
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
            Raises:
                NoDatabaseConnection: If engine for some reason can't connect to database
        '''
        return await self.start_(Users_API, Users_DB, "postgresql+asyncpg://release:horse_ate_green_guinea_pig@localhost/db")
    
    async def is_email_registered(self, email: str) -> bool:
        '''
            Method that checks if login is in database
            Args:
                login(str): login (email in our case)
            Returns:
                bool: True if already in database
        '''
        return len(await self.api.get_by_email(email)) == 0
    
    async def register(self, email: str, password: str) -> None:
        '''
            Method that register new user.
            Args:
                email(str): user's email
                password(str): user's password
            Returns:
                NoneType:
            Raises:
                NotUnique: If email is not unique
        '''
        if await self.is_email_registered(email):
            raise NotUnique("Email is not unique")

        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) # encoding password
        await self.api.register(
            email=email,
            password=password
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
            raise NotExist("User does not exist")
        
        return (await self.api.get_by_email(email))[0]

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
            raise NotExist("User does not exist")
        
        return bcrypt.checkpw(password.encode(), (await self.api.get_by_email(email))[0]["password"])