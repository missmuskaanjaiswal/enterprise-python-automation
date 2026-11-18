
import json
from datetime import datetime
from pathlib import Path


def generate_report(data, output_dir="reports"):
    """Generate and save an automation report."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report = {
        "generated_at": datetime.now().isoformat(),
        "total_records": len(data),
        "status": "completed",
        "data": data
    }

    filename = output_path / "automation_report.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return str(filename)
  
