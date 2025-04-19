from typing_extensions import Self, Literal, List, Optional
from pydantic import BaseModel, Field

from datetime import datetime


class ProductSchema(BaseModel):
    productId: int
    supplierId: int
    title: str
    titleImage: str
    cost: int
    description: str

    @staticmethod
    async def parse(ProductObj) -> Self:
        return ProductSchema(
            productId=ProductObj.productId,
            supplierId=ProductObj.supplierId,
            title=ProductObj.title,
            titleImage=ProductObj.titleImage,
            cost=ProductObj.cost,
            description=ProductObj.description
        )

class OrderSchema(BaseModel):
    orderId: int

    costumerFirstName: str
    costumerSecondName: Optional[str]
    comment: Optional[str]
    phoneNumber: Optional[str]

    isFinished: bool
    isCanceled: bool

    country: str
    city: str
    street: str
    building: str
    flat: str

    userId: int
    productId: int

    orderStatus: str
    orderCreatedTimestamp: int

    @staticmethod
    async def parse(ProductObj, GeoObj) -> Self:
        return OrderSchema(
            orderId = ProductObj.userId,
            costumerFirstName = ProductObj.costumerFirstName,
            costumerSecondName = ProductObj.costumerSecondName,
            comment = ProductObj.comment,
            phoneNumber = ProductObj.comment,
            isFinished = ProductObj.isFinished,
            isCanceled = ProductObj.isCanceled,

            country = GeoObj.country,
            city = GeoObj.city,
            street = GeoObj.street,
            building = GeoObj.building,
            flat = GeoObj.flat,

            userId = ProductObj.userId,
            productId = ProductObj.productId,

            orderStatus = ProductObj.orderStatus,
            orderCreatedTimestamp = ProductObj.orderCreatedTime
        )
    
class ProductSchemasArray(BaseModel):
    ProductSchemasArray: list[ProductSchema]

class OrderSchemasArray(BaseModel):
    OrderSchemasArray: list[OrderSchema]

class EmptyModel(BaseModel):
    pass