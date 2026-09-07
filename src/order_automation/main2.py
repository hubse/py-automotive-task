def main():

    settings = load_settings()

    orders_directory = Path(settings.orders_directory)
    report_directory = Path(settings.report_directory)

    report_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    report_path = report_directory / "orders.xlsx"

    file_reader = OrderFileReader()

    shipping_api = ShippingApi(
        base_url=settings.shipping_api_url,
    )

    excel_generator = ExcelReportGenerator()

    email_sender = EmailSender(
        smtp_host=settings.smtp_host,
        smtp_port=settings.smtp_port,
        username=settings.smtp_username,
        password=settings.smtp_password,
    )

    processor = OrderProcessor(
        shipping_service=shipping_api,
    )

    processed_orders = []

    for file in orders_directory.glob("*.txt"):

        try:
            order = file_reader.read(file)

            processed = processor.process(order)

            processed_orders.append(processed)

        except (OSError, ValueError) as exc:
            print(f"Skipping {file}: {exc}")

    excel_generator.generate(
        processed_orders,
        str(report_path),
    )

    email_sender.send(
        recipient=settings.report_recipient,
        subject="Daily Orders Report",
        body="Today's order report is attached.",
        attachment=str(report_path),
    )

    print("Report successfully generated.")


if __name__ == "__main__":
    main()

