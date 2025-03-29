import traceback
import asyncio
import bcrypt

from typing import Self, List

from exceptions.database_exceptions import *
from settings import DBSettings

from database.ProductAdditionalImagesAPI import ProductAdditionalImagesAPI
from database.ProductAdditionalImagesDB import ProductAdditionalImagesDB

from schemas.ProductAdditionalImagesSchemas import *
from schemas.RPCSchemas import *

from simple_rpc import GrpcServer

app = GrpcServer()

class ProductAdditionalImages():
    def __init__(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `ProductAdditionalImages` object
        '''
        self.ProductAdditionalImagesAPI = ProductAdditionalImagesAPI(
            ProductAdditionalImagesDB,
            DBSettings.DATABASE_URL
        )
    
    @app.grpc_method()
    async def add_images(
            self,
            request: AddImagesRequest
        ) -> EmptyModel:

        for img in request.imageUrls:
            await self.ProductAdditionalImagesAPI.add_image(
                imageUrl=img,
                productId=request.productId
            )
        return EmptyModel()
    
    @app.grpc_method()
    async def get_images_by_productId(
            self,
            request: ProductIdModel
        ) -> AdditionalImagesDTOArray:
        result = await self.ProductAdditionalImagesAPI.get_images_url_by_productId(
            productId=request.productId
        )
        return AdditionalImagesDTOArray(
            AdditionalImagesDTOArray=[
                AdditionalImagesDTO(
                    id=image.id,
                    productId=image.productId,
                    imageUrl=image.imageUrl
                )
                for image in result
            ]
        )

app.configure_service(
    cls=ProductAdditionalImages(),
    port=50504
)
app.run()