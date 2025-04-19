from pydantic import BaseModel

class UserSchema(BaseModel):
    userId: int
    type: str
    isConfirmed: bool
    isSupplierStatusConfirmed: bool
    isAdmin: bool
