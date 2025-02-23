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
class SecuritySettings():
    SECURITY_KEY = "e859fa584aeb78113af2ac7846cd0a5b28d96a56ecc60ec247e6eb4f4d503cec6fc2618687e92432363ddd602f4a80f6bd3d48fead411a229dd8665a7e11c699" # openssl rand -hex 64
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 1
    ALGORYTM = "HS512"

    # uncomment this before building container!
    # DATABASE_URL = "postgresql+asyncpg://release:horse_ate_green_guinea_pig@postgres/db"

    DATABASE_URL = "postgresql+asyncpg://release:horse_ate_green_guinea_pig@localhost/db"

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