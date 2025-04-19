from typing import Self, List, Any

from exceptions.database_exceptions import *
from settings import DBSettings

from database.CatalogAPI import CatalogAPI
from database.CatalogDB import CatalogDB

from schemas.CatalogSchemas import *
from schemas.RPCScemas import *

from simple_rpc import GrpcServer

app = GrpcServer()

class Catalog():
    def __init__(self) -> Self:
        '''
            Method that starts connection to database
            Returns:
                `Catalog` object
        '''
        self.CatalogAPI = CatalogAPI(CatalogDB, DBSettings.DATABASE_URL)

    @app.grpc_method()
    async def get_products(
            self,
            request: GetProductsRequest
        ) -> ProductDTOArray:

        if request.sort == "time_descending":
            result = await self.CatalogAPI.get_all_products_time_desc(
                    start = request.start,
                    count = request.count
                )
            
        elif request.sort == "time_upscending":
            result = await self.CatalogAPI.get_all_products_time_upsc(
                    start = request.start,
                    count = request.count
                )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
        return ProductDTOArray(
            productDTOArray=[ 
                await ProductDTO.parse(product)
                for product in result
            ]
        )
    
    @app.grpc_method()
    async def get_product_by_id(
            self,
            request: ProductIdModel
        ) -> ProductDTO:

        product = await self.CatalogAPI.get_product_by_id(
            productId=request.productId
        )
        return await ProductDTO.parse(product)

    @app.grpc_method()
    async def add_product(self,
            request: AddProductRequest
        ) -> ProductIdModel:
        '''
            Method that creates product
        '''

        return ProductIdModel(
            productId=await self.CatalogAPI.create_product(
                title=request.title,
                titleImageUrl=request.titleImageUrl,
                costNum=request.costNum,
                description=request.description,
                authorId=request.authorId
            )
        )
    
    @app.grpc_method()
    async def get_my_products(
            self,
            request: GetMyProductsRequest
        ) -> ProductDTOArray:

        if request.sort == "time_descending":
            result = await self.CatalogAPI.get_my_products_time_desc(
                userId = request.userId,
                start = request.start,
                count = request.count
            )
        elif request.sort == "time_upscending":
            result = await self.CatalogAPI.get_my_products_time_upsc(
                    userId = request.userId,
                    start = request.start,
                    count = request.count
                )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
        return ProductDTOArray(
            productDTOArray=[ 
                await ProductDTO.parse(product)
                for product in result
            ]
        )
    
    @app.grpc_method()
    async def get_all_my_products(
            self,
            request: UserIdModel
        ) -> ProductDTOArray:

        result = await self.CatalogAPI.get_all_my_products(
            userId = request.userId
        )
        return ProductDTOArray(
            productDTOArray=[ 
                await ProductDTO.parse(product)
                for product in result
            ]
        )
    
    # BAD SEARCH FUNCTION!
    # TODO: REWRITE IT!
    @app.grpc_method()
    async def search_in_title(
            self,
            request: SearchRequest
        ) -> ProductDTOArray:

        if request.sort == "time_descending":
            result =  await self.CatalogAPI.search_title_contains_time_desc(
                request.phrase,
                request.start,
                request.count
            )
        elif request.sort == "time_upscending":
            result = await self.CatalogAPI.search_title_contains_time_upsc(
                request.phrase,
                request.start,
                request.count
            )
        else:
            raise Developing("Sorry, this sort type is unimplemeted. We're already working on it...")
        
        return ProductDTOArray(
            productDTOArray=[ 
                await ProductDTO.parse(product)
                for product in result
            ]
        )

app.configure_service(
    cls=Catalog(),
    port=50505
)
app.run()