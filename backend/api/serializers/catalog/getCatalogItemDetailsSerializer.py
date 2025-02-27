from libs.database import ProductAdditionalImages, Users

class getCatalogItemDetailsSerializer:
    @classmethod
    async def start(cls):
       self = cls()

       self.AdditionalImagesAPI = await ProductAdditionalImages.start()
       self.UsersAPI = await Users.start()
       return self

    async def serialize(self, data):
        imagesUrls = await self.AdditionalImagesAPI.get_images_by_productId(
            productId=data["id"]
        )
        print(imagesUrls)
        email = (await self.UsersAPI.get_by_id(
            id=data["supplierId"]
        ))["email"]

        print(imagesUrls)

        return {
            "title": data["title"],
            "author": email,
            "titleImage": data["titleImage"],
            "productId": data["id"],
            "cost": {
                "currency": "RUB",
                "costNum": data["cost"]
            },
            "reviews": { #fake block
                "rank": 4.0,
                "reviewsCount": 10
            },
            "description": data["description"],
            "boughtTimesCounter": 100, # fake
            "additionalImages": [image["imageUrl"] for image in imagesUrls]
        }