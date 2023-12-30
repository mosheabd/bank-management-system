import re
from datetime import datetime


def validate_full_name(full_name):
    parts = full_name.split()
    if len(parts) < 2:
        return False, "Full name must include at least first and last name."
    if any(not part.isalpha() for part in parts):
        return False, "Full name must only contain alphabetic characters."
    return True, "Valid"


def validate_email(email):
    if "@" not in email or len(email.split('@')) != 2:
        return False, "Invalid email format. Email must contain '@'."
    return True, "Valid"


def validate_address(address):
    # Basic checks for an address
    if len(address) < 10 or len(address) > 100:
        return False, "Address length should be between 10 and 100 characters."

    # Check for the presence of at least one numeral (common in addresses)
    if not any(char.isdigit() for char in address):
        return False, "Address should contain at least one numeral."

    # Check for the presence of alphabetic characters (common in street names)
    if not any(char.isalpha() for char in address):
        return False, "Address should contain letters."

    return True, "Valid"


def validate_phone_number(phone_number):
    if not re.match(r'^0\d{1,2}-\d{7}$', phone_number):
        return False, "Invalid phone number format. Must be 0x-xxxxxxx or 0xx-xxxxxxx."
    return True, "Valid"


def validate_birth_date(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
    except ValueError:
        return False, "Invalid date format. Use DD/MM/YYYY."

    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    if age < 18:
        return False, "You must be at least 18 years old to open an account."
    return True, "Valid"
