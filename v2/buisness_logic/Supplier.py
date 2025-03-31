from typing_extensions import List, Self, Optional
from exceptions.basic_exception import BasicException

from simple_rpc import GrpcClient, GrpcServer

from commands.CatalogCommands import CatalogCommands
from commands.AdditionalImagesCommands import AdditionalImagesCommands
from commands.OrderCommands import OrderCommands
from commands.GeoCommands import GeoCommands


from output_schemas.SupplierSchemas import *

from input_schemas.Supplier import *

import asyncio

CatalogClient = GrpcClient(
    port=50505,
    ip="catalog_controller",
    proto_file_relpath="protos/Catalog.proto"
)
CatalogCommandsManager = CatalogCommands(
    client = CatalogClient
)

AdditionalImagesClient = GrpcClient(
    port=50504,
    ip="product_additional_images_controller",
    proto_file_relpath="protos/ProductAdditionalImages.proto"
)
AdditionalImagesCommandsManager = AdditionalImagesCommands(
    client = AdditionalImagesClient
)

OrderClient = GrpcClient(
    port=50503,
    ip="order_controller",
    proto_file_relpath="protos/Order.proto"
)
OrderCommandsManager = OrderCommands(
    client = OrderClient
)

GeoClient = GrpcClient(
    port=50506,
    ip="geo_controller",
    proto_file_relpath="protos/Geo.proto"
)
GeoCommandsManager = GeoCommands(
    client = GeoClient
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
        return EmptyModel()
    
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
    
    @app.grpc_method()
    async def orders_for_me(
            self,
            request: UserIdReq
        ) -> OrderSchemasArray:

        productsArr = await CatalogCommandsManager.get_all_my_products(
            userId=request.userId
        )

        activeOrders = []
        for product in productsArr.productDTOArray:
            activeOrders.extend(
                (
                    await OrderCommandsManager.get_active_with_productId(
                        productId=product.productId
                    )
                ).OrderDTOArray
            )
        
        return OrderSchemasArray(
            OrderSchemasArray=[
                await OrderSchema.parse(
                    ProductObj=order,
                    GeoObj=await GeoCommandsManager.get_geo_by_id(
                        geoId=order.geoId
                    )
                )
                for order in activeOrders
            ]
        )
    
    @app.grpc_method()
    async def set_status(
            self,
            request: SetOrderStatusReq
        ) -> EmptyModel:
        await OrderCommandsManager.set_status_by_id(
            orderId=request.orderId,
            newStatus=request.newStatus
        )
        return EmptyModel()

    @app.grpc_method()
    async def finish_order(
            self,
            request: OrderIdReq
        ) -> EmptyModel:
        await OrderCommandsManager.finish_by_id(
            orderId=request.orderId
        )
        return EmptyModel()

app.configure_service(
    cls=SupplierLogic(),
    port=50515
)
app.run()