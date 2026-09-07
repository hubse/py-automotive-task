from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    customer: str
    country: str
    amount: Decimal


@dataclass
class ProcessedOrder:
    customer: str
    country: str
    amount: Decimal
    shipping: Decimal

    @property
    def total(self) -> Decimal:
        return self.amount + self.shipping
