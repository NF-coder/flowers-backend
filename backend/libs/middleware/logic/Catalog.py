from ..main.Catalog import Catalog
from .schemas.CatalogSchemas import *

from ..main.Users import Users

from ..main.ProductAdditionalImages import ProductAdditionalImages

from typing_extensions import List
from exceptions import BasicException

Catalog = Catalog()
Users = Users()
AdditionalImages = ProductAdditionalImages()

class CatalogLogic():
    @staticmethod
    def __init__(self) -> Self:
        pass

    async def get_product_by_id(
        id: int    
    ) -> ProductSchema:
        product = await Catalog.get_product_by_id(
            id=id
        )
        supplier = await Users.get_info_by_id(
            id=product.supplierId
        )

        return await ProductSchema.parse(
            UserObj=supplier,
            ProductObj=product
        )

    async def get_catalog_item_details(
            id: int
        ) -> ProductDetailsSchema:
        product = await Catalog.get_product_by_id(
            id=id
        )
        supplier = await Users.get_info_by_id(
            id=product.supplierId
        )
        additionalImagesUrls = [image.imageUrl
            for image in await AdditionalImages.get_images_by_productId(
                productId=product.productId
            )
        ]

        return await ProductDetailsSchema.parse(
            UserObj=supplier,
            ProductObj=product,
            AdditionalImagesArr=additionalImagesUrls
        )
    
    async def get_catalog(
            start: int,
            count: int,
            sort: str
        ) -> List[ProductSchema]:
        products = await Catalog.get_products(
            start=start,
            count=count, 
            sort=sort
        )

        out = []

        for product in products:
            supplier = await Users.get_info_by_id(id=product.supplierId)
            
            out.append(
                await ProductSchema.parse(
                    UserObj=supplier,
                    ProductObj=product
                )
            )
        return out
    
    async def search(
            req: str,
            start: int,
            count: int,
            sort: str
        ) -> List[ProductSchema]:

        productArr = await Catalog.search_in_title(
            phrase=req,
            start=start,
            count=count,
            sort=sort
        )
        out = []
        for product in productArr:
            supplier = await Users.get_info_by_id(id=product.supplierId)
            
            out.append(
                await ProductSchema.parse(
                    UserObj=supplier,
                    ProductObj=product
                )
            )

        return out