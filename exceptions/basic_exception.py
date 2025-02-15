from dataclasses import dataclass

@dataclass
class HttpException(Exception):
    code: int = 500
    description: str = "Error occured"