Order Automation

Automated order-processing application that reads order files, retrieves shipping costs from an external API, processes the data, generates an Excel report, and sends the report by email.

Architecture


                         ┌─────────────────┐
                         │    Scheduler    │
                         │  Cron / Task    │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     main.py     │
                         │ Composition Root│
                         └────────┬────────┘
                                  │
                                  ▼
                  ┌──────────────────────────────┐
                  │         Application          │
                  │                              │
                  │      OrderProcessor          │
                  │      Business Logic          │
                  └──────────────┬───────────────┘
                                 │
                            Interfaces
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       File Storage         Shipping API         Email
       Adapter              Adapter              Adapter
              │                  │                  │
              ▼                  ▼                  ▼
          Filesystem          REST API             SMTP
                                  
                         ┌─────────────────┐
                         │ Excel Generator │
                         └────────┬────────┘
                                  │
                                  ▼
                                pandas



Project Structure

```text
order_automation/
│
├── pyproject.toml
├── README.md
├── .env
├── .gitignore
│
├── src/
│   └── order_automation/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       │
│       ├── domain/
│       │   ├── __init__.py
│       │   ├── models.py
│       │   └── exceptions.py
│       │
│       ├── application/
│       │   ├── __init__.py
│       │   └── services/
│       │       ├── __init__.py
│       │       └── order_processor.py
│       │
│       └── infrastructure/
│           ├── __init__.py
│           ├── file_storage.py
│           ├── shipping_api.py
│           ├── excel_report.py
│           └── email_sender.py
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_order_processor.py
│   │
│   └── integration/
│       ├── __init__.py
│       └── test_order_pipeline.py
│
└── data/
    ├── orders/
    ├── reports/
    └── tmp/
```

Requirements

Python 3.11+
pip or uv
Access to the shipping API
SMTP credentials for sending email
Setup

1. Clone the repository
git clone <repository-url>
cd order_automation

2. Create a virtual environment
python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

macOS/Linux:

source .venv/bin/activate

3. Install dependencies
pip install -e ".[dev]"

Input Files

Place order files in:
data/orders/

```text
data/orders/
├── order_001.txt
├── order_002.txt
└── order_003.txt
```

Expected format:
Customer: Ali
Amount: 250.00
Country: Pakistan

Running the Application

Run the application directly:
python -m order_automation.main


If the CLI entry point is configured in pyproject.toml:
order-automation

The application will:

Read order files
      ↓
Parse order information
      ↓
Retrieve shipping cost
      ↓
Process orders
      ↓
Generate Excel report
      ↓
Send report by email


The generated report will be placed under:
data/reports/

Testing

Run all tests:
pytest


Run unit tests:
pytest tests/unit

Run integration tests:
pytest tests/integration


Run with coverage:
pytest --cov=order_automation
