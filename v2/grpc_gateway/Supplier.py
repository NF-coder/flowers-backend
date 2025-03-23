from ..main.Catalog import Catalog
from ..main.Users import Users
from ..main.Order import Order
from ..main.Geo import Geo
from ..main.ProductAdditionalImages import ProductAdditionalImages

from .schemas.SupplierSchemas import *

from typing_extensions import List, Self, Optional
from exceptions import BasicException

Catalog = Catalog()
Users = Users()
Order = Order()
Geo = Geo()
ProductAdditionalImages = ProductAdditionalImages()

class SupplierLogic():
    @staticmethod
    def __init__(self) -> None:
        pass
    
    async def add_product(
            title: str,
            titleImageUrl: str,
            costNum: int,
            description: str,
            authorId: int,
            additionalImagesUrls: str,
        ) -> None:

        productId = await Catalog.add_product(
            title=title,
            titleImageUrl=titleImageUrl,
            costNum=costNum,
            description=description,
            authorId=authorId
        )
        await ProductAdditionalImages.add_images(
            imageUrls=additionalImagesUrls,
            productId=productId
        )
    
    async def my_products_list(
            userId: int,
            start: int,
            count: int,
            sort: str
        ) -> List[ProductSchema]:

        products = await Catalog.get_my_products(
            userId=userId,
            start=start,
            count=count,
            sort=sort
        )

        return [
            await ProductSchema.parse(
                ProductObj=product
            )
            for product in products
        ]
    
    async def orders_for_me(
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
            orderId: int,
            newStatus: str
        ) -> None:
        await Order.set_status_by_id(
            id=orderId,
            newStatus=newStatus
        )

    async def finish_order(
            orderId: int
        ) -> None:
        await Order.finish_by_id(
            id=orderId
        )