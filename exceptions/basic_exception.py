from dataclasses import dataclass

@dataclass
class HttpException(Exception):
    '''
        REST API Exception dataclass, which handles in `main.py`
        Attributes:
            code (int): HTTP statuscode of error
            description (str): Description of error
    '''
    code: int = 500
    description: str = "Error occured"