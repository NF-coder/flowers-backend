from typing_extensions import Self
from pydantic import BaseModel, model_validator

class UnicornException(Exception):
    def __init__(self, code: int, output: dict):
        self.code = code
        self.output = output

class SignIn(BaseModel):
    basic_token: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        '''
            Check if Basic token has valid format
        '''
        if self.basic_token[:6] != "Basic ":
            raise ValueError('Passwords do not match')
        return self