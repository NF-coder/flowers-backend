from libs.database import Geo, OrderProducts

class orderInfoSerializer:
    @classmethod
    async def start(cls):
       self = cls()

       self.GeoAPI = await Geo.start()
       self.OrderProductsAPI = await OrderProducts.start()
       return self

    async def serialize(self, data):
        
        adress = await self.GeoAPI.get_by_id(
            id=data["geoId"]
        )

        productsArr = await self.OrderProducts.get_by_orderId(
            orderId=data["id"]
        )

        return {
            "orderId": data["id"],
            "adress": {
                "Contry": adress["country"],
                "City": adress["city"],
                "Street": adress["street"],
                "Building": adress["building"],
                "Flat": adress["flat"]
            },
            "orderStatus": data["orderStatus"],
            "orderCreatedTime": data["orderCreatedTime"],
            "customerPhone": data["phoneNumber"],
            "customerFirstName": data["customerFirstName"],
            "customerSecondName": data["customerSecondName"],
            "comment": data["comment"],
            "productIdArray": [elem["productId"] for elem in productsArr]
        }