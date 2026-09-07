import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:

    app_env: str
    log_level: str

    shipping_api_url: str
    shipping_api_key: str

    smtp_host: str
    smtp_port: int
    smtp_username: str
    smtp_password: str

    report_recipient: str

    orders_directory: str
    report_directory: str


def load_settings() -> Settings:

    return Settings(
        app_env=os.environ["APP_ENV"],
        log_level=os.environ["LOG_LEVEL"],

        shipping_api_url=os.environ["SHIPPING_API_URL"],
        shipping_api_key=os.environ["SHIPPING_API_KEY"],

        smtp_host=os.environ["SMTP_HOST"],
        smtp_port=int(os.environ["SMTP_PORT"]),
        smtp_username=os.environ["SMTP_USERNAME"],
        smtp_password=os.environ["SMTP_PASSWORD"],

        report_recipient=os.environ["REPORT_RECIPIENT"],

        orders_directory=os.environ["ORDERS_DIRECTORY"],
        report_directory=os.environ["REPORT_DIRECTORY"],
    )

