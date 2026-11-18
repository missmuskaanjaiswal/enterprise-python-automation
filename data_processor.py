
import json
from typing import Any


def process_data(data: Any) -> dict:
    """Process incoming data and return a summary."""

    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            return {
                "status": "error",
                "message": "Invalid JSON data"
            }

    if isinstance(data, list):
        return {
            "status": "success",
            "total_records": len(data),
            "data": data
        }

    if isinstance(data, dict):
        return {
            "status": "success",
            "total_records": 1,
            "data": data
        }

    return {
        "status": "error",
        "message": "Unsupported data format"
    }
  
