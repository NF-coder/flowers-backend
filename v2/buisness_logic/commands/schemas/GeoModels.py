from pydantic import BaseModel, Field

class GeoDTO(BaseModel):
    geoId: int
    userId: int

    country: str
    city: str
    street: str
    building: str
    flat: str

class GeoId(BaseModel):
    id: int