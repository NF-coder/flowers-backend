import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from ..database.api.TgIdAuthAPI import TgIdAuthAPI
from ..database.fields.TgIdAuthDB import TgIdAuthDB

class TgIdAuth():
    def __init__(self) -> Self:
        self.TgIdAuthAPI = TgIdAuthAPI(TgIdAuthDB, SecurityConfig.DATABASE_URL)

    async def add_auth_method(self, tgId: int, userId: int) -> None:
        await self.TgIdAuthAPI.add_auth_method(
            tgId=tgId,
            userId=userId
        )
    
    async def remove_auth_method(self, tgId: int) -> None:
        await self.TgIdAuthAPI.remove_auth_method(
            tgId=tgId
        )