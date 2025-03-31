from .schemas.AdditionalImagesModels import *

from simple_rpc import GrpcClient

class AdditionalImagesCommands():
    def __init__(self, client: GrpcClient) -> None:
        self.add_images__ = client.configure_command(
            functionName="add_images",
            className="ProductAdditionalImages"
        )
        self.get_images_by_productId__ = client.configure_command(
            functionName="get_images_by_productId",
            className="ProductAdditionalImages"
        )
    
    async def add_images(self, imageUrls: list[str], productId: int):
        await self.add_images__(
            imageUrls=imageUrls,
            productId=productId
        )
    
    async def get_images_by_productId(self, productId: int) -> AdditionalImagesDTOArray:
        return AdditionalImagesDTOArray.model_validate(
            await self.get_images_by_productId__(
                productId = productId
            ),
            from_attributes=True
        )