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
            AVAILABLE_ACCOUNT_TYPES(`list` of `str`):
                Available account types list. Used for validation while registration
            EMAIL_CHECKER_REGEX(str):
                Email regex. Used for validation while registration
            BASIC_TOKEN_REGEX(str):
                Basic token regex. Used for validation while sign-in
    '''
    AVAILABLE_ACCOUNT_TYPES = ["costumer", "supplier"]
    BASIC_TOKEN_REGEX = r"^Basic .+"
    EMAIL_CHECKER_REGEX = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

@dataclass
class TgBotApiAcess:
    API_KEY = "53b0afa34ced8d853aaad6983f6264c60b20d3d311533b22df8740caf4e0475192823a3434a5f76adbafca26e0838b089fc921edceebefd9b83e4796946b4d40"