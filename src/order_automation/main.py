from pathlib import Path

from order_automation.application.services.order_processor import (
    OrderProcessor,
)

from order_automation.infrastructure.file_storage import (
    OrderFileReader,
)

from order_automation.infrastructure.shipping_api import (
    ShippingApi,
)

from order_automation.infrastructure.excel_report import (
    ExcelReportGenerator,
)

from order_automation.infrastructure.email_sender import (
    EmailSender,
)


def main():

    orders_directory = Path("data/orders")
    report_path = "data/reports/orders.xlsx"

    # Infrastructure
    file_reader = OrderFileReader()

    shipping_api = ShippingApi(
        base_url="https://example.com/api"
    )

    excel_generator = ExcelReportGenerator()

    email_sender = EmailSender(
        smtp_host="smtp.company.com",
        smtp_port=587,
        username="reports@company.com",
        password="SECRET",
    )

    # Application
    processor = OrderProcessor(
        shipping_service=shipping_api
    )

    processed_orders = []

    # Process files
    for file in orders_directory.glob("*.txt"):

    try:
        order = file_reader.read(file)

        processed = processor.process(order)

        processed_orders.append(processed)

    except (OSError, ValueError) as exc:
        print(f"Skipping {file}: {exc}")

    # Generate report
    excel_generator.generate(
        processed_orders,
        report_path,
    )

    # Send email
    email_sender.send(
        recipient="manager@company.com",
        subject="Daily Orders Report",
        body="Today's order report is attached.",
        attachment=report_path,
    )

    print("Report successfully generated.")


if __name__ == "__main__":
    main()

