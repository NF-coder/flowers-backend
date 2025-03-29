from pydantic import BaseModel

class ListSuppliersRequestsReq(BaseModel):
    start: int
    count: int
    sort: str

class ApproveSupplierRequestReq(BaseModel):
    id: int