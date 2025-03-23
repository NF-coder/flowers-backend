from typing_extensions import Self, Literal, List
from pydantic import BaseModel, Field

from database.GeoDB import GeoDB

class GeoDTO(BaseModel):
    geoId: int
    userId: int

    country: str
    city: str
    street: str
    building: int
    flat: str

    @staticmethod
    async def parse(obj: GeoDB) -> Self:
        return GeoDTO(
            geoId=obj.id,
            userId=obj.userId,
            
            country=obj.country,
            city=obj.city,
            street=obj.street,
            building=obj.building,
            flat=obj.flat
        )