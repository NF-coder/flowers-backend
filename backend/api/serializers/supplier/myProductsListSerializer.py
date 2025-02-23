from libs.database import Users

class myProductsListSerializer:
    @classmethod
    async def start(cls):
       self = cls()

       self.UsersAPI = await Users.start()
       return self

    async def serializeItem(self, data):
        email = (await self.UsersAPI.get_by_id(
            id=data["supplierId"]
        ))["email"]

        return {
            "title": data["title"],
            "author": email,
            "image": data["titleImage"],
            "productId": data["id"],
            "cost": {
                "currency": "RUB",
                "costNum": data["cost"]
            },
            "reviews": { #fake block
                "rank": 4.0,
                "reviewsCount": 10
            }
        }