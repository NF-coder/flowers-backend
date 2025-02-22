from backend.libs.database import Users
from backend.libs.tokens import Tokens

import asyncio

async def make_admin(email: str) -> str:
    API = await Users.start()
    await API.make_admin_by_email(email)

    user = await API.get_by_email(email)

    user.pop("password")
    token, _ = await Tokens.get_acess_token(**user)
    print(token)

if __name__=="__main__":
    asyncio.run(
        make_admin(email="example@example.com")
    )