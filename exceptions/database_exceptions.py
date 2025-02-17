from dataclasses import dataclass

@dataclass
class NotUnique(Exception):
    '''
        Database Exception dataclass. Signals, that object, that must be unique
        does not.
        Attributes:
            description (str): Description of error
    '''
    description: str = "Error occured"

@dataclass
class NotExist(Exception):
    '''
        Database Exception dataclass. Signals, that object, that must exist 
        does not exist
        Attributes:
            description (str): Description of error
    '''
    description: str = "Error occured"

@dataclass
class NoDatabaseConnection(Exception):
    '''
        Database Exception dataclass. Signals, that database API can't connect to database
        does not exist
        Attributes:
            description (str): Description of error
    '''
    description: str = "Error occured"