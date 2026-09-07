from typing import Protocol
from decimal import Decimal

from order_automation.domain.models import (
    Order,
    ProcessedOrder,
)


class ShippingService(Protocol):

    def get_shipping_cost(
        self,
        country: str,
    ) -> Decimal:
        ...


class OrderProcessor:

    def __init__(
        self,
        shipping_service: ShippingService,
    ):
        self.shipping_service = shipping_service

    def process(
        self,
        order: Order,
    ) -> ProcessedOrder:

        shipping = self.shipping_service.get_shipping_cost(
            order.country
        )

        return ProcessedOrder(
            customer=order.customer,
            country=order.country,
            amount=order.amount,
            shipping=shipping,
        )

