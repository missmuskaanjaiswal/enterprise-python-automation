
import argparse
import json

from enterprise_automation.data_processor import process_data
from enterprise_automation.report_generator import generate_report


def main():
    parser = argparse.ArgumentParser(
        description="Enterprise Python Automation Tool"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input JSON file"
    )

    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as file:
            raw_data = json.load(file)

        result = process_data(raw_data)

        if result["status"] == "error":
            print(result["message"])
            return

        report_path = generate_report(result["data"])
        print(f"Report generated successfully: {report_path}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")


if __name__ == "__main__":
    main()
  
