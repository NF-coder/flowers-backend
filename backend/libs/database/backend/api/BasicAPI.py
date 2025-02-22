#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from typing import Self

from exceptions.database_exceptions import NoDatabaseConnection

class BasicAPI:
    @classmethod # Cause I can't use asyncio in __magic__ functions, so...
    async def start(cls, base_fields, base_url) -> Self:
        '''
            Method that starts connection to database
            Args:
                base_fields(`declarative_base()` inheritor?):
                    Schema of databse. Can be found in backend.fields
                base_url(str):
                    Link to database. Starts with (for example): `postgresql+asyncpg://`
            Returns:
                self:
            Raises:
                NoDatabaseConnection: If engine for some reason can't connect to database
        '''
        try:
            self = cls()

            self.base = base_fields
            self.engine = create_async_engine(base_url)

            await self.init_db()

            self.session = sessionmaker(
                bind = self.engine,
                class_ = AsyncSession,
                expire_on_commit = False
            )

        except Exception as exc:
            raise NoDatabaseConnection(
                description="Error while connecting to database! [DB_API]"
            )
            #print(f"Error while API init:\n{traceback.format_exc()}\n")

        return self
    
    async def init_db(self): # special function for database startup
        async with self.engine.begin() as conn:
            await conn.run_sync(self.base.metadata.create_all)