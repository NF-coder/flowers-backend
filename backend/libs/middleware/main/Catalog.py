from typing import Self, List, Any

from exceptions.database_exceptions import *
from settings import SecurityConfig

from ..database.api.CatalogAPI import CatalogAPI
from ..database.fields.CatalogDB import CatalogDB

from .schemas.CatalogSchemas import *

class Catalog():
    def __init__(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `Catalog` object
        '''
        self.CatalogAPI = CatalogAPI(CatalogDB, SecurityConfig.DATABASE_URL)

    async def get_products(
            self,
            start: int,
            count: int,
            sort: str,
        ) -> List[ProductDTO]:

        if sort == "time_descending":
            result = await self.CatalogAPI.get_all_products_time_desc(
                    start = start,
                    count = count
                )
            
        elif sort == "time_upscending":
            result = await self.CatalogAPI.get_all_products_time_upsc(
                    start = start,
                    count = count
                )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
        return [ 
            await ProductDTO.parse(product)
            for product in result
        ]
        
    async def get_product_by_id(
            self,
            id: int
        ) -> ProductDTO:

        product = await self.CatalogAPI.get_product_by_id(
            productId=id
        )
        return await ProductDTO.parse(product)

    async def add_product(self,
            title: str,
            titleImageUrl: str,
            costNum: int,
            description: str,
            authorId: int
        ) -> int:
        '''
            Method that creates product
        '''

        return await self.CatalogAPI.create_product(
            title=title,
            titleImageUrl=titleImageUrl,
            costNum=costNum,
            description=description,
            authorId=authorId
        )
    
    async def get_my_products(
            self,
            userId: int,
            start: int,
            count: int,
            sort: str,
        ) -> list[ProductDTO]:

        if sort == "time_descending":
            result = await self.CatalogAPI.get_my_products_time_desc(
                userId = userId,
                start = start,
                count = count
            )
        elif sort == "time_upscending":
            result = await self.CatalogAPI.get_my_products_time_upsc(
                    userId = userId,
                    start = start,
                    count = count
                )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
        return [ 
            await ProductDTO.parse(product)
            for product in result
        ]
    
    # BAD SEARCH FUNCTION!
    # TODO: REWRITE IT!
    async def search_in_title(
            self,
            phrase: str,
            start: int,
            count: int,
            sort: str
        ) -> List[ProductDTO]:
        pass
        '''if CatalogSession is None:
            CatalogSession = await self.CatalogAPI.startSession()
        if AdditionalImagesSession is None:
            AdditionalImagesSession = await self.AdditionalImagesAPI()

        if sort == "time_descending":
            return await CatalogSession.search_title_contains_time_desc(
                phrase,
                start,
                count
            )
        elif sort == "time_upscending":
            return await CatalogSession.search_title_contains_time_upsc(
                phrase,
                start,
                count
            )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")'''