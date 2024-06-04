import re
from typing import Tuple


def return_json(success, message, data=None, status_code=500):
    """Create response for api"""
    return {
        "Success": success,
        "Message": message,
        "Data": data
    }, status_code


def valid_satellite_name(name: str) -> Tuple[bool, str]:

    # Check if the string is None or empty
    if not name:
        return False, "ID cannot be null or empty."

    # Check for special characters or whitespace
    if re.search(r'[^\w-]', name):
        return False, "ID contains invalid characters. Only alphanumeric characters and hyphens are allowed."

    # Check for minimum and maximum length constraints
    if len(name) < 3:
        return False, "ID must be at least 3 characters long."
    if len(name) > 255:
        return False, "ID must not exceed 255 characters."

    return True, "Valid ID"
