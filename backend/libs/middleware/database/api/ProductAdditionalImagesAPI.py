#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from typing import Self, Dict, List

from .BasicAPI import BasicAPI

from exceptions.database_exceptions import NoDatabaseConnection

# For type annotations
from ..fields.ProductAdditionalImagesDB import ProductAdditionalImagesDB
DatabaseType = ProductAdditionalImagesDB

class ProductAdditionalImagesAPI(BasicAPI):
    async def add_image(
            self,
            imageUrl: str,
            productId: int
        ) -> int:
        '''
            Method that adds image to database
            Args:
                imageUrl(str) - url of image
            Returns:
                int: id of image
        '''
        statement = self.base(
            imageUrl=imageUrl,
            productId=productId
        )
        async with self.session() as session:
            session.add(statement)
            await session.commit()
    
    async def get_images_url_by_productId(
            self,
            productId: int
        ) -> List[DatabaseType]:
        statement = select(self.base).where(self.base.productId == productId)

        async with self.session() as session:
            out = await session.execute(statement)
        return out