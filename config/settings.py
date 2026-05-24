"""Global configuration settings."""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"

# Ensure data directory exists
DATA_DIR.mkdir(exist_ok=True)

# Data file paths
STUDENTS_FILE = DATA_DIR / "students.json"
CLASSES_FILE = DATA_DIR / "classes.json"
EXAMS_FILE = DATA_DIR / "exams.json"
GRADES_FILE = DATA_DIR / "grades.json"

# Application settings
APP_NAME = "Student Management System"
APP_VERSION = "1.0.0"
DEBUG = True

# Logging
LOG_FILE = PROJECT_ROOT / "logs" / "app.log"
LOG_LEVEL = "INFO"

# Validation rules
MIN_STUDENT_AGE = 5
MAX_STUDENT_AGE = 80
MIN_SCORE = 0
MAX_SCORE = 10

# Default values
DEFAULT_CLASS_SIZE = 30
DEFAULT_EXAM_ROOM_CAPACITY = 30
