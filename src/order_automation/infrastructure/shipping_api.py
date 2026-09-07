from decimal import Decimal
import requests


class ShippingApi:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_shipping_cost(
        self,
        country: str,
    ) -> Decimal:

        response = requests.get(
            f"{self.base_url}/shipping",
            params={"country": country},
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        return Decimal(str(data["price"]))

