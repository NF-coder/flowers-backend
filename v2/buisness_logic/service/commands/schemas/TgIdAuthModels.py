from pydantic import BaseModel

class UserIdModel(BaseModel):
    userId: int