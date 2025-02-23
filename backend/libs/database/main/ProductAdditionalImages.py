import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from .Basic import Basic

from ..backend.api.ProductAdditionalImagesAPI import ProductAdditionalImagesAPI
from ..backend.fields.ProductAdditionalImagesDB import ProductAdditionalImagesDB

class ProductAdditionalImages(Basic):
    @classmethod
    async def start(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `ProductAdditionalImages` object
        '''
        return await self.start_(
            ProductAdditionalImagesAPI,
            ProductAdditionalImagesDB,
            SecurityConfig.DATABASE_URL
        )
    
    # Использовалось на одной из итераций принятия говнокода. На данный момент не используется
    async def get_orm_image_object(self, imageUrl: str) -> ProductAdditionalImagesDB:
        '''
            Method that starts connection to database
            Returns:
                `ProductAdditionalImagesDB` object
        '''
        return await self.api.get_orm_image_object(
            imageUrl=imageUrl
        )
    
    async def add_images(
            self,
            imageUrls: List[str],
            productId: int
        ) -> None:

        for img in imageUrls:
            await self.api.add_image(
                imageUrl=img,
                productId=productId
            )
    
    async def get_images_by_productId(
            self,
            productId: int
        ):
        return await self.api.get_images_url_by_productId(
                productId=productId
            )