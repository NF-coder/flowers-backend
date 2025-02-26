from libs.database import Users
from libs.tokens import Tokens

from libs.database.backend.api.UsersAPI import UsersAPI
from libs.database.backend.fields.UsersDB import UsersDB

import asyncio

async def make_admin(email: str) -> str:
    # Docker: postgresql+asyncpg://release:horse_ate_green_guinea_pig@postgres/db
    # Local: postgresql+asyncpg://release:horse_ate_green_guinea_pig@localhost/db
    API = await Users.start_(UsersAPI, UsersDB, "postgresql+asyncpg://release:horse_ate_green_guinea_pig@localhost/db")

    await API.make_admin_by_email(email)

    user = await API.get_by_email(email)

    user.pop("password")
    token, _ = await Tokens.get_acess_token(**user)
    print(token)

if __name__=="__main__":
    asyncio.run(
        make_admin(email="example@example.com")
    )