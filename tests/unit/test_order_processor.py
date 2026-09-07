from decimal import Decimal

from order_automation.application.services.order_processor import (
    OrderProcessor,
)
from order_automation.domain.models import Order


class FakeShippingService:

    def get_shipping_cost(self, country: str) -> Decimal:
        return Decimal("10.00")


def test_order_processor_calculates_total():

    shipping_service = FakeShippingService()

    processor = OrderProcessor(
        shipping_service=shipping_service
    )

    order = Order(
        customer="Ali",
        country="Pakistan",
        amount=Decimal("100.00"),
    )

    result = processor.process(order)

    assert result.customer == "Ali"
    assert result.country == "Pakistan"
    assert result.amount == Decimal("100.00")
    assert result.shipping == Decimal("10.00")
    assert result.total == Decimal("110.00")

