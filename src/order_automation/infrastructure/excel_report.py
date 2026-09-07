import pandas as pd

from order_automation.domain.models import ProcessedOrder


class ExcelReportGenerator:

    def generate(
        self,
        orders: list[ProcessedOrder],
        output_path: str,
    ):

        rows = [
            {
                "Customer": order.customer,
                "Country": order.country,
                "Order": float(order.amount),
                "Shipping": float(order.shipping),
                "Total": float(order.total),
            }
            for order in orders
        ]

        df = pd.DataFrame(rows)

        df.to_excel(
            output_path,
            index=False,
        )

