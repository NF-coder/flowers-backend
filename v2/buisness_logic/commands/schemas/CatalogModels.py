from pydantic import BaseModel

class ProductDTO(BaseModel):
    productId: int
    supplierId: int
    title: str
    titleImage: str
    cost: int
    description: str

class ProductId(BaseModel):
    productId: int

class ProductDTOArray(BaseModel):
    productDTOArray: list[ProductDTO]

class ProductDetailsDTO(ProductDTO):
    additionalImages: list[str]

# unused

class GetProductsRequest(BaseModel):
    start: int
    count: int
    sort: str



class UserIdModel(BaseModel):
    userId: int

class GetMyProductsRequest(BaseModel):
    userId: int
    start: int
    count: int
    sort: str

class AddProductRequest(BaseModel):
    title: str
    titleImageUrl: str
    costNum: int
    description: str
    authorId: int


    




