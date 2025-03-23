#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from typing import Self

from exceptions.database_exceptions import NoDatabaseConnection

import asyncio
import traceback

class BasicAPI:
    def __init__(self, base_fields, base_url) -> Self:
        # Cause I want to see types annotation
        self.base = base_fields
        self.base_url = base_url
        self = self.startORM()

    
    def startORM(self) -> Self:
        '''
            Method that starts connection to database
            Args:
                base_fields(`DeclarativeBase`):
                    Schema of databse. Can be found in backend.fields
                base_url(str):
                    Link to database. Starts with (for example): `postgresql+asyncpg://`
            Returns:
                self:
            Raises:
                NoDatabaseConnection: If engine for some reason can't connect to database
        '''
        cls = self
        try:
            cls.engine = create_async_engine(cls.base_url)
            
            #loop_ = asyncio.new_event_loop()
            asyncio.ensure_future(BasicAPI.createAll(cls.engine, cls.base))
    
            
            cls.session = sessionmaker(
                bind = cls.engine,
                class_ = AsyncSession,
                expire_on_commit = False
            )
            

        except Exception as exc:
            print(traceback.format_exc())
            raise NoDatabaseConnection(
                description="Error while connecting to database! [DB_Basic_API]"
            )

        return cls
    
    @staticmethod
    async def createAll(engine, base):
        async with engine.begin() as conn:
            await conn.run_sync(base.metadata.create_all)