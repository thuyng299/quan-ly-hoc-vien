"""Validation utilities for data input."""

import re
from datetime import datetime
from config.settings import (
    MIN_STUDENT_AGE,
    MAX_STUDENT_AGE,
    MIN_SCORE,
    MAX_SCORE,
)


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    """Validate Vietnamese phone number format."""
    pattern = r"^(0|\+84)[0-9]{9,10}$"
    return re.match(pattern, phone) is not None


def validate_id_number(id_number: str) -> bool:
    """Validate ID number (CCCD/CMND) format."""
    return len(id_number) in [9, 12] and id_number.isdigit()


def validate_date_of_birth(dob: str) -> bool:
    """Validate date of birth and check age range."""
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        return MIN_STUDENT_AGE <= age <= MAX_STUDENT_AGE
    except ValueError:
        return False


def validate_score(score: float) -> bool:
    """Validate score range."""
    try:
        score_float = float(score)
        return MIN_SCORE <= score_float <= MAX_SCORE
    except (ValueError, TypeError):
        return False


def validate_student_id(student_id: str) -> bool:
    """Validate student ID format."""
    pattern = r"^SV\d{6}$"
    return re.match(pattern, student_id) is not None


def validate_not_empty(value: str, field_name: str = "Field") -> tuple[bool, str]:
    """Validate that a string field is not empty."""
    if not value or not value.strip():
        return False, f"{field_name} không được để trống"
    return True, ""
