from .schemas.CatalogCommandsSchemas import *

from simple_rpc import GrpcClient

class CatalogCommands:
    def __init__(self, client: GrpcClient) -> None:
        self.get_product_by_id__ = client.configure_command(
            functionName="get_product_by_id",
            className="CatalogLogic"
        )
        self.get_catalog_item_details__ = client.configure_command(
            functionName="get_catalog_item_details",
            className="CatalogLogic"
        )
        self.get_catalog__ = client.configure_command(
            functionName="get_catalog",
            className="CatalogLogic"
        )
        self.search__ = client.configure_command(
            functionName="search",
            className="CatalogLogic"
        )
    
    async def get_product_by_id(self, productId: int) -> ProductSchema:
        responce =  await self.get_product_by_id__(
            id = productId
        )
        return ProductSchema(
            productId=responce.productId,
            supplierId=responce.supplierId,
            title=responce.title,
            titleImage=responce.title,
            cost=responce.cost,
            description=responce.description
        )

    async def get_catalog_item_details(self, productId: int) -> ProductDetailsSchema:
        responce =  await self.get_catalog_item_details__(
            id = productId
        )
        return ProductDetailsSchema(
            productId=responce.productId,
            supplierId=responce.supplierId,
            title=responce.title,
            titleImage=responce.title,
            cost=responce.cost,
            description=responce.description,
            additionalImages=responce.additionalImages
        )

    async def get_catalog(self, start: int, count: int, sort: str) -> list[ProductSchema]:
        responce =  await self.get_catalog__(
            start = start,
            count = count,
            sort = sort
        )
        return [
            ProductSchema(
                productId=product.productId,
                supplierId=product.supplierId,
                title=product.title,
                titleImage=product.title,
                cost=product.cost,
                description=product.description
            )
            for product in responce.ProductSchemasArray
        ]
    
    async def search(self, request: str, start: int, count: int, sort: str) -> list[ProductSchema]:
        responce =  await self.search__(
            req = request,
            start = start,
            count = count,
            sort = sort
        )
        return [
            ProductSchema(
                productId=product.productId,
                supplierId=product.supplierId,
                title=product.title,
                titleImage=product.title,
                cost=product.cost,
                description=product.description
            )
            for product in responce.ProductSchemasArray
        ]