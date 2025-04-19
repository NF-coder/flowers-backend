from .schemas.CatalogModels import *

from simple_rpc import GrpcClient

class CatalogCommands():
    def __init__(self, client: GrpcClient) -> None:
        self.get_product_by_id__ = client.configure_command(
            functionName="get_product_by_id",
            className="Catalog"
        )
        self.add_product__ = client.configure_command(
            functionName="add_product",
            className="Catalog"
        )
        self.get_products__ = client.configure_command(
            functionName="get_products",
            className="Catalog"
        )
        self.get_my_products__ = client.configure_command(
            functionName="get_my_products",
            className="Catalog"
        )
    
        self.search_in_title__ = client.configure_command(
            functionName="search_in_title",
            className="Catalog"
        )
        self.get_all_my_products__ = client.configure_command(
            functionName="get_all_my_products",
            className="Catalog"
        )

    async def get_product_by_id(self, productId: int) -> ProductDTO:
        return ProductDTO.model_validate(
            await self.get_product_by_id__(
                productId = productId
            ),
            from_attributes=True
        )
    
    async def add_product(self, title: str, titleImageUrl: str, costNum: int, description: str, authorId: int) -> ProductId:
        return ProductId.model_validate(
            await self.add_product__(
                title=title,
                titleImageUrl=titleImageUrl,
                costNum=costNum,
                description=description,
                authorId=authorId
            ),
            from_attributes=True
        )
    
    async def get_products(self, start: int, count: int, sort: str) -> ProductDTOArray:
        return ProductDTOArray.model_validate(
            await self.get_products__(
                start=start,
                count=count, 
                sort=sort
            ),
            from_attributes=True
        )
    
    async def get_my_products(self, userId: int, start: int, count: int, sort: str) -> ProductDTOArray:
        return ProductDTOArray.model_validate(
            await self.get_my_products__(
                userId=userId,
                start=start,
                count=count,
                sort=sort
            ),
            from_attributes=True
        )
    
    async def search_in_title(self, phrase: str, start: int, count: int, sort: str) -> ProductDTOArray:
        return ProductDTOArray.model_validate(
            await self.search_in_title__(
                phrase=phrase,
                start=start,
                count=count,
                sort=sort
            ),
            from_attributes=True
        )
    
    async def get_all_my_products(self, userId: int) -> ProductDTOArray:
        return ProductDTOArray.model_validate(
            await self.get_all_my_products__(
                userId=userId
            ),
            from_attributes=True
        )