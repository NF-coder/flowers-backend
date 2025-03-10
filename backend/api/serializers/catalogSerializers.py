from libs.middleware.logic.schemas.CatalogSchemas import *
from validation.components.CostDict import CostDict
from validation.components.ReviewsDict import ReviewsDict

class catalogSerializers:
    @staticmethod
    def __init__(self): pass

    async def getCatalogItemDetailsSerializer(
            data: ProductDetailsSchema,
            ResponceModel,
            CostDictModel: CostDict,
            ReviewDictModel: ReviewsDict
        ):
        return ResponceModel(
            title=data.title,
            author=data.supplierEmail,
            titleImage=data.titleImage,
            additionalImages=data.additionalImages,
            cost=CostDictModel(
                costNum=data.cost
            ),
            reviews=ReviewDictModel(),
            description=data.description
        )
    
    async def getCatalogSerializer(
            data: List[ProductSchema],
            ResponceModel,
            CostDictModel: CostDict,
            ReviewDictModel: ReviewsDict
        ):
        return [
            ResponceModel(
                title=product.title,
                author=product.supplierEmail,
                image=product.titleImage,
                productId=product.productId,
                cost=CostDictModel(
                    costNum=product.cost
                ),
                reviews=ReviewDictModel()
            )
            for product in data
        ]