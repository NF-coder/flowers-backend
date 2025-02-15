from dataclasses import dataclass

@dataclass
class HttpException(Exception):
    code: int
    description: [str = "Error occured" | str]