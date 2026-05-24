"""File handling utilities for import/export operations."""

import json
from pathlib import Path
from typing import Any, Dict, List
from utils.logger import get_logger

logger = get_logger(__name__)


def read_json_file(file_path: Path) -> List[Dict[str, Any]]:
    """Read data from JSON file."""
    try:
        if not file_path.exists():
            logger.info(f"File {file_path} not found, returning empty list")
            return []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(f"Successfully read {len(data)} records from {file_path}")
            return data
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        return []


def write_json_file(file_path: Path, data: List[Dict[str, Any]]) -> bool:
    """Write data to JSON file."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Successfully wrote {len(data)} records to {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error writing to file {file_path}: {str(e)}")
        return False


def export_to_csv(file_path: Path, data: List[Dict[str, Any]]) -> bool:
    """Export data to CSV file."""
    try:
        import csv
        
        if not data:
            logger.warning("No data to export")
            return False
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        logger.info(f"Successfully exported {len(data)} records to {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error exporting to CSV {file_path}: {str(e)}")
        return False


def import_from_csv(file_path: Path) -> List[Dict[str, Any]]:
    """Import data from CSV file."""
    try:
        import csv
        
        if not file_path.exists():
            logger.warning(f"File {file_path} not found")
            return []
        
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        
        logger.info(f"Successfully imported {len(data)} records from {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error importing from CSV {file_path}: {str(e)}")
        return []
