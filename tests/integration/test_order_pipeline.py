from decimal import Decimal
from pathlib import Path

from order_automation.application.services.order_processor import (
    OrderProcessor,
)
from order_automation.infrastructure.file_storage import (
    OrderFileReader,
)


class FakeShippingService:

    def get_shipping_cost(self, country: str) -> Decimal:
        return Decimal("15.00")


def test_order_file_to_processed_order(tmp_path: Path):

    order_file = tmp_path / "order.txt"

    order_file.write_text(
        """Customer: Ali
Amount: 100.00
Country: Pakistan
"""
    )

    reader = OrderFileReader()

    order = reader.read(order_file)

    processor = OrderProcessor(
        shipping_service=FakeShippingService()
    )

    result = processor.process(order)

    assert result.customer == "Ali"
    assert result.amount == Decimal("100.00")
    assert result.shipping == Decimal("15.00")
    assert result.total == Decimal("115.00")

