import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from ..database.api.EmailAuthAPI import EmailAuthAPI
from ..database.fields.EmailAuthDB import EmailAuthDB

class EmailAuth():
    def __init__(self) -> Self:
        self.EmailAuthAPI = EmailAuthAPI(EmailAuthDB, SecurityConfig.DATABASE_URL)

    async def add_auth_method(self, email: str, password: str, userId: int) -> None:
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()) # encoding password
        await self.EmailAuthAPI.add_auth_method(
            email=email,
            password=password,
            userId=userId
        )
    
    async def remove_auth_method(self, email: str) -> None:
        await self.EmailAuthAPI.remove_auth_method(
            email=email
        )