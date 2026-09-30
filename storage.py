import json
from pathlib import Path

DATA_FILE = Path("data/students.json")

def load_students():
    """Read student records from the JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with an empty list.")
        return []

def save_students(students):
    """Save all student records to the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
