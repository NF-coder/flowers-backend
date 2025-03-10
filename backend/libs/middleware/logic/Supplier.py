from ..main.Catalog import Catalog
from ..main.Geo import Geo
from ..main.ProductAdditionalImages import ProductAdditionalImages

from .schemas.OrderSchemas import *

from typing_extensions import List, Self, Optional
from exceptions import BasicException

Catalog = Catalog()
Geo = Geo()
ProductAdditionalImages = ProductAdditionalImages()

class SupplierLogic():
    @staticmethod
    def __init__(self) -> Self:
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
    
    #async def my_products_list(
    #    userId: int,
    #    start: int,
    #    count: int,
    #    sort: str
    #):