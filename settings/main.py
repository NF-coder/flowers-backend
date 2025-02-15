from dataclasses import dataclass

@dataclass
class Settings:
    '''
        Main settings of app
        Attributes:
            API_VERSION (int): version of API
    '''
    API_VERSION = 1

@dataclass
class AuthSettings:
    '''
        Settings of auth
        Attributes:
            AVAILABLE_ACCOUNT_TYPES (:obj:`list` of :obj:`int`): version of API
    '''
    AVAILABLE_ACCOUNT_TYPES = ["costumer", "supplier"]
    BASIC_TOKEN_REGEX = r"^Basic .+"
    EMAIL_CHECKER_REGEX = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"