from .schemas.GeoModels import *

from simple_rpc import GrpcClient

class GeoCommands():
    def __init__(self, client: GrpcClient) -> None:
        self.add_geo__ = client.configure_command(
            functionName="add_geo",
            className="Geo"
        )
        self.get_geo_by_id__ = client.configure_command(
            functionName="get_by_id",
            className="Geo"
        )
    
    async def add_geo(
            self,
            country: str,
            city: str,
            street: str,
            building: str,
            flat: str,
            userId: int
        ) -> GeoId:
        return GeoId.model_validate(
            await self.add_geo__(
                country=country,
                city=city,
                street=street,
                building=building,
                flat=flat,
                userId=userId
            ),
            from_attributes=True
        )
    
    async def get_geo_by_id(
            self,
            geoId: int
        ) -> GeoDTO:
        return GeoDTO.model_validate(
            await self.get_geo_by_id__(
                id=geoId
            ),
            from_attributes=True
        )