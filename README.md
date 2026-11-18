Enterprise Python Automation

RabTech Academy Software Engineering Internship | Capstone Project

Overview

Enterprise Python Automation is a Python-based application designed to automate data collection, processing, task scheduling, and report generation.

The project provides a modular structure for managing automation tasks and generating structured JSON reports.

Features

- API client integration
- Automated data processing
- JSON data validation
- Background task scheduling
- Automated JSON report generation
- Command-line interface (CLI)
- Error handling and logging
- Unit testing

Technologies Used

- Python
- Requests
- APScheduler
- JSON
- Argparse
- Unittest

Project Structure

enterprise-python-automation/
│
├── src/
│   └── enterprise_automation/
│       ├── __init__.py
│       ├── api_client.py
│       ├── main.py
│       ├── data_processor.py
│       ├── scheduler.py
│       ├── report_generator.py
│       └── cli.py
│
├── tests/
│   └── test_automation.py
│
├── requirements.txt
├── pyproject.toml
├── sample_data.json
└── README.md

Installation

Clone the repository:

git clone https://github.com/missmuskaanjaiswal/enterprise-python-automation.git

Navigate to the project directory:

cd enterprise-python-automation

Install dependencies:

pip install -r requirements.txt

Install the project:

pip install -e .

Usage

Run the automation application:

enterprise-automation --input sample_data.json

Alternatively, run using Python:

python -m enterprise_automation.cli --input sample_data.json

Report Generation

The application processes input JSON data and generates an automated JSON report.

Generated reports are stored in the "reports/" directory.

Task Scheduling

The project uses APScheduler to support background task scheduling at configurable time intervals.

Testing

Run automated unit tests:

python -m unittest discover -s tests

The tests cover:

- List data processing
- Dictionary data processing
- Invalid JSON handling

Error Handling

The application handles common errors such as:

- Missing input files
- Invalid JSON data
- Unsupported data formats

Author

Muskaan Jaiswal

License

This project is developed for educational and internship purposes.
