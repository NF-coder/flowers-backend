from typing_extensions import List
from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient, GrpcServer
from commands.UsersCommands import UsersCommands
from commands.CatalogCommands import CatalogCommands
from commands.AdditionalImagesCommands import AdditionalImagesCommands

from input_schemas.Catalog import *
from output_schemas.CatalogSchemas import *

import asyncio

UsersClient = GrpcClient(
    port=50501,
    ip="ussrs_controller",
    proto_file_relpath="protos/Users.proto"
)
CatalogClient = GrpcClient(
    port=50505,
    ip="catalog_controller",
    proto_file_relpath="protos/Catalog.proto"
)
AdditionalImagesClient = GrpcClient(
    port=50504,
    ip="product_additional_images_controller",
    proto_file_relpath="protos/ProductAdditionalImages.proto"
)
AdditionalImagesCommandsManager = AdditionalImagesCommands(
    client = AdditionalImagesClient
)
UsersCommandsManager = UsersCommands(
    client = UsersClient
)
CatalogCommandsManager = CatalogCommands(
    client = CatalogClient
)
app = GrpcServer()

class CatalogLogic():
    def __init__(self) -> None:
        pass

    @app.grpc_method()
    async def get_product_by_id(
        self,
        request: ProductIdReq
    ) -> ProductSchema:
        product = await CatalogCommandsManager.get_product_by_id(
            productId=request.id
        )

        return await ProductSchema.parse(
            ProductObj=product
        )

    @app.grpc_method()
    async def get_catalog_item_details(
            self,
            request: ProductIdReq
        ) -> ProductDetailsSchema:
        product = await CatalogCommandsManager.get_product_by_id(
            productId=request.id
        )
        additionalImagesUrls = [image.imageUrl
            for image in (await AdditionalImagesCommandsManager.get_images_by_productId(
                productId=product.productId
            )).AdditionalImagesDTOArray
        ]

        return await ProductDetailsSchema.parse(
            ProductObj=product,
            AdditionalImagesArr=additionalImagesUrls
        )
    
    @app.grpc_method()
    async def get_catalog(
            self,
            request: GetCatalogReq
        ) -> ProductSchemasArray:
        products = await CatalogCommandsManager.get_products(
            start=request.start,
            count=request.count, 
            sort=request.sort
        )

        return ProductSchemasArray(
            ProductSchemasArray=[
                await ProductSchema.parse(
                    ProductObj=product
                )
                for product in products.productDTOArray
            ]
        )
    
    @app.grpc_method()
    async def search(
            self,
            request: SearchReq
        ) -> ProductSchemasArray:
        products = await CatalogCommandsManager.search_in_title(
            phrase=request.req,
            start=request.start,
            count=request.count,
            sort=request.sort
        )
        return ProductSchemasArray(
            ProductSchemasArray=[
                await ProductSchema.parse(
                    ProductObj=product
                )
                for product in products.productDTOArray
            ]
        )

app.configure_service(
    cls=CatalogLogic(),
    port=50513
)
app.run()