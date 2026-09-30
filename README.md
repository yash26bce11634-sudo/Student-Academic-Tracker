# Student Academic Tracker

A beginner-level Python console project to store student records, enter marks, and generate academic summaries.

## Features
- Add, view, update, and delete student records
- Enter or update subject marks (0–100)
- View an individual student's marks and average
- View a class summary and class average
- Save data locally in a JSON file
- Basic input validation and unit tests

## Technologies
- Python 3
- JSON for local storage
- `unittest` for basic tests
- Git and GitHub for version control

## Requirements
Python 3. No third-party packages are required.

## Run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run: `python main.py`

On some systems, use `python3 main.py`.

## Test
From the project folder, run:
`python -m unittest discover -s tests`

## Data
Student information is stored in `data/students.json`. Keep this file if you want to preserve records. Do not enter sensitive real student information in a public repository.

## Project structure
- `main.py` — menu and program flow
- `student_manager.py` — student CRUD operations
- `marks_manager.py` — marks entry
- `reports.py` — averages and reports
- `storage.py` — JSON loading and saving
- `validators.py` — input checks and student lookup
- `tests/test_tracker.py` — basic tests
- `data/students.json` — saved records
