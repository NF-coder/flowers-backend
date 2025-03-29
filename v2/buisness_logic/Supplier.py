from typing_extensions import List, Self, Optional
from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient, GrpcServer
from commands.CatalogCommands import CatalogCommands
from commands.AdditionalImagesCommands import AdditionalImagesCommands

from output_schemas.SupplierSchemas import *

from input_schemas.Supplier import *

import asyncio

CatalogClient = GrpcClient(
    port=50505,
    proto_file_relpath="protos/Catalog.proto"
)
CatalogCommandsManager = CatalogCommands(
    client = CatalogClient
)
AdditionalImagesClient = GrpcClient(
    port=50504,
    proto_file_relpath="protos/ProductAdditionalImages.proto"
)
AdditionalImagesCommandsManager = AdditionalImagesCommands(
    client = AdditionalImagesClient
)
app = GrpcServer()

class SupplierLogic():
    def __init__(self) -> None:
        pass
    
    @app.grpc_method()
    async def add_product(
            self,
            request: AddProductReq
        ) -> EmptyModel:

        catalogResponce = await CatalogCommandsManager.add_product(
            title=request.title,
            titleImageUrl=request.titleImageUrl,
            costNum=request.costNum,
            description=request.description,
            authorId=request.authorId
        )
        await AdditionalImagesCommandsManager.add_images(
            imageUrls=request.additionalImagesUrls,
            productId=catalogResponce.productId
        )
    
    @app.grpc_method()
    async def my_products_list(
            self,
            request: MyProductsListReq
        ) -> ProductSchemasArray:

        products = await CatalogCommandsManager.get_my_products(
            userId=request.userId,
            start=request.start,
            count=request.count,
            sort=request.sort
        )

        return ProductSchemasArray(
            ProductSchemasArray = [
                await ProductSchema.parse(
                    ProductObj=product
                )
                for product in products.productDTOArray
            ]
        )
    
    async def orders_for_me(
            self,
            userId: int
        ) -> List[OrderSchema]:

        productsArr = await Catalog.get_all_my_products(
            userId=userId
        )
        activeOrders = []
        for product in productsArr:
            activeOrders.extend(
                await Order.get_active_with_productId(
                    productId=product.productId
                )
            )
        
        return [
            await OrderSchema.parse(
                ProductObj=order,
                GeoObj=await Geo.get_by_id(
                    id=order.geoId
                )
            )
            for order in activeOrders
        ]
    
    async def set_status(
            self,
            orderId: int,
            newStatus: str
        ) -> None:
        await Order.set_status_by_id(
            id=orderId,
            newStatus=newStatus
        )

    async def finish_order(
            self,
            orderId: int
        ) -> None:
        await Order.finish_by_id(
            id=orderId
        )

app.configure_service(
    cls=SupplierLogic(),
    port=50515
)
app.run()