from typing_extensions import Self
from pydantic import BaseModel, Field, field_validator

class RequestModel(BaseModel):
    tgId: int = Field(
        frozen=True,
        description="User's tg-id",
        example="12345678"
    )
    type: str = Field(frozen=True, description="Account type")
    
class RequestHeadersModel(BaseModel):
    Key: str = Field(
        frozen=True,
        description="автризация для бота. костыль!",
        example="AAABBBCCC"
    )

class ResponceSchema(BaseModel):
    '''
        Responce schema for /api/{version}/auth/registerBasic
        Attributes:
            token (str): user's jwt token
    '''
    token: str = Field(default="Bearer AAA.BBB.CCC")