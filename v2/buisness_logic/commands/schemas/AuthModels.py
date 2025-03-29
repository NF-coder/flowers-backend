from pydantic import BaseModel

class CheckPasswordResponce(BaseModel):
    status: bool
    userId: int