from dataclasses import dataclass
from .basic_exception import BasicException

@dataclass
class CantDecodeJWT(BasicException):
    '''
        Token Exception dataclass. Signals, that library can't decode JWT for some reason.
    '''
    def __post_init__(self): self.code = 400

@dataclass
class CantDecodeBasicToken(BasicException):
    '''
        Token Exception dataclass. Signals, that library can't decode Basic token for some reason.
    '''
    def __post_init__(self): self.code = 400

@dataclass
class ExpiredJWT(BasicException): # Not used
    '''
        Token Exception dataclass. Signals, that JWT token is expired
    '''
    def __post_init__(self): self.code = 400