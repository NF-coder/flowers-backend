import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .Basic import Basic
from .ProductAdditionalImages import ProductAdditionalImages
from .Users import Users

from ..backend.api.GeoAPI import GeoAPI
from ..backend.fields.GeoDB import GeoDB

class Geo(Basic):
    @classmethod
    async def start(self) -> Self:
        return await self.start_(GeoAPI, GeoDB, SecurityConfig.DATABASE_URL)
    

    async def add_geo(
        self,
        country: str,
        city: str,
        street: str,
        building: str,
        flat: str,
        userId: int
    ) -> int:
        return await self.api.add_geo(
            country=country,
            city=city,
            street=street,
            building=building,
            flat=flat,
            userId=userId
        )
    
    async def get_by_id(
        self,
        id: int
    ) -> dict:
        return await self.api.get_by_id(
            id=id
        )