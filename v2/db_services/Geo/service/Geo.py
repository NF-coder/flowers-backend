from exceptions.database_exceptions import *
from settings import DBSettings

from database.GeoAPI import GeoAPI
from database.GeoDB import GeoDB

from schemas.GeoSchemas import *
from schemas.RPCSchemas import *

from simple_rpc import GrpcServer

app = GrpcServer()

class Geo():
    def __init__(self) -> None:
        self.GeoAPI = GeoAPI(GeoDB, DBSettings.DATABASE_URL)

    @app.grpc_method()
    async def add_geo(
        self,
        request: AddGeoRequest
    ) -> GeoIdModel:
        return GeoIdModel(
            id = await self.GeoAPI.add_geo(
                country=request.country,
                city=request.city,
                street=request.street,
                building=request.building,
                flat=request.flat,
                userId=request.userId
            )
        )

    @app.grpc_method()
    async def get_by_id(
        self,
        request: GeoIdModel
    ) -> GeoDTO:
        result = await self.GeoAPI.get_by_id(
            id=request.id
        )
        return await GeoDTO.parse(result)

# SimpleRPC server startup

app.configure_service(
    cls=Geo(),
    port=50506
)
app.run()
