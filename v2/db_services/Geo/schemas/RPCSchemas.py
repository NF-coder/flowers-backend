from typing_extensions import Self, Literal
from pydantic import BaseModel, Field

class GeoIdModel(BaseModel):
    id: int
class AddGeoRequest(BaseModel):
    country: str
    city: str
    street: str
    building: str
    flat: str
    userId: int