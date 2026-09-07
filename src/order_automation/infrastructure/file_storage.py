from pathlib import Path
import re
from decimal import Decimal, InvalidOperation

from order_automation.domain.models import Order


class OrderFileReader:

    def read(self, file: Path) -> Order:

        text = file.read_text(encoding="utf-8")

        customer_match = re.search(
            r"^Customer:\s*(.+)$",
            text,
            re.MULTILINE,
        )

        amount_match = re.search(
            r"^Amount:\s*([\d.]+)$",
            text,
            re.MULTILINE,
        )

        country_match = re.search(
            r"^Country:\s*(.+)$",
            text,
            re.MULTILINE,
        )

        if not customer_match:
            raise ValueError(
                f"Missing Customer field in {file}"
            )

        if not amount_match:
            raise ValueError(
                f"Missing Amount field in {file}"
            )

        if not country_match:
            raise ValueError(
                f"Missing Country field in {file}"
            )

        customer = customer_match.group(1).strip()
        country = country_match.group(1).strip()

        if not customer:
            raise ValueError(
                f"Customer cannot be empty in {file}"
            )

        if not country:
            raise ValueError(
                f"Country cannot be empty in {file}"
            )

        try:
            amount = Decimal(amount_match.group(1))
        except InvalidOperation as exc:
            raise ValueError(
                f"Invalid Amount in {file}"
            ) from exc

        if amount < 0:
            raise ValueError(
                f"Amount cannot be negative in {file}"
            )

        return Order(
            customer=customer,
            country=country,
            amount=amount,
        )

