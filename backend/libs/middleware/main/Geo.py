import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .ProductAdditionalImages import ProductAdditionalImages
from .Users import Users

from ..database.api.GeoAPI import GeoAPI
from ..database.fields.GeoDB import GeoDB

from .schemas.GeoSchemas import *


class Geo():
    def __init__(self) -> Self:
        self.GeoAPI = GeoAPI(GeoDB, SecurityConfig.DATABASE_URL)

    async def add_geo(
        self,
        country: str,
        city: str,
        street: str,
        building: str,
        flat: str,
        userId: int
    ) -> int:
        
        return await self.GeoAPI.add_geo(
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
    ) -> GeoDTO:
        result = await self.GeoAPI.get_by_id(
            id=id
        )
        return await GeoDTO.parse(result)