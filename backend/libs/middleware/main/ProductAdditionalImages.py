import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import SecurityConfig

from ..database.api.ProductAdditionalImagesAPI import ProductAdditionalImagesAPI
from ..database.fields.ProductAdditionalImagesDB import ProductAdditionalImagesDB

from .schemas.ProductAdditionalImagesSchemas import AdditionalImagesDTO

class ProductAdditionalImages():
    def __init__(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `ProductAdditionalImages` object
        '''
        self.ProductAdditionalImagesAPI = ProductAdditionalImagesAPI(
            ProductAdditionalImagesDB,
            SecurityConfig.DATABASE_URL
        )
    
    async def add_images(
            self,
            imageUrls: List[str],
            productId: int
        ) -> None:

        for img in imageUrls:
            await self.ProductAdditionalImagesAPI.add_image(
                imageUrl=img,
                productId=productId
            )
    
    async def get_images_by_productId(
            self,
            productId: int,
        ) -> List[AdditionalImagesDTO]:
        result = await self.ProductAdditionalImagesAPI.get_images_url_by_productId(
                productId=productId
        )
        return [
            AdditionalImagesDTO(
                id=image.id,
                productId=image.productId,
                imageUrl=image.imageUrl
            )
            for image in result
        ]