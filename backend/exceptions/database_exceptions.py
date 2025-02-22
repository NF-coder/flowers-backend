from dataclasses import dataclass
from .basic_exception import BasicException

@dataclass
class NotUnique(BasicException):
    '''
        Database Exception dataclass. Signals, that object, that must be unique
        does not.
    '''
    def __post_init__(self): self.code = 400

@dataclass
class NotExist(BasicException):
    '''
        Database Exception dataclass. Signals, that object, that must exist 
        does not exist
    '''
    def __post_init__(self): self.code = 400

@dataclass
class NotEnoudhArguments(BasicException):
    '''
        Database Exception dataclass. Signals, that there're not enough of specified arguments.
    '''
    def __post_init__(self): self.code = 400


@dataclass
class NoDatabaseConnection(BasicException):
    '''
        Database Exception dataclass. Signals, that database API can't connect to database
        does not exist
    '''
    def __post_init__(self): self.code = 500