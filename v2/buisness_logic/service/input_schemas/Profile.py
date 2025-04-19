from pydantic import BaseModel

class UserIdReq(BaseModel):
    userId: int

class EmptyModel(BaseModel):
    pass