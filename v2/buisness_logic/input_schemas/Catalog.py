from pydantic import BaseModel

class ProductIdReq(BaseModel):
    id: int

class GetCatalogReq(BaseModel):
    start: int
    count: int
    sort: str