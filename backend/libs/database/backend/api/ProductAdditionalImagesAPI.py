#Required lib import
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import select, update, delete, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

import asyncio
import traceback
import os
from typing import Self, Dict, List

from ..utils.utils import Middleware_utils
from .BasicAPI import BasicAPI

from exceptions.database_exceptions import NoDatabaseConnection

class ProductAdditionalImagesAPI(BasicAPI):

    # Used for relations() in ORM, but not enough time to fix bugs with ORM...
    async def image_object(
            self,
            imageUrl: str
        ) -> object:
        '''
            Method that returns ORM object of `ProductAdditionalImagesDB`
            Args:
                imageUrl(str) - url of image
            Returns:
                ProductAdditionalImagesDB:
        '''
        statement = self.base(
            imageUrl=imageUrl
        )
        return statement
    
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
        ) -> List[str]:
        statement = select(self.base.imageUrl).where(self.base.productId == productId)

        async with self.session() as session:
            out = await session.execute(statement)

        return await Middleware_utils.db_answer_to_dict(
                                                        out,
                                                        table_name = self.base.__name__,
                                                        column_mode = True
                    )
