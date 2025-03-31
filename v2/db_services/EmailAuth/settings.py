from dataclasses import dataclass

@dataclass
class DBSettings():
    # uncomment this before building container!
    DATABASE_URL = "postgresql+asyncpg://release:horse_ate_green_guinea_pig@postgres/db"

    # uncomment for local database
    #DATABASE_URL = "postgresql+asyncpg://release:horse_ate_green_guinea_pig@localhost/db"