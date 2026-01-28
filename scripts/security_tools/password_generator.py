# password_generator.py

import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        use_uppercase (bool): Include uppercase letters (A-Z).
        use_lowercase (bool): Include lowercase letters (a-z).
        use_digits (bool): Include digits (0-9).
        use_symbols (bool): Include symbols (e.g., !@#$%^&*).

    Returns:
        str: The generated password.

    Raises:
        ValueError: If no character types are selected or length is non-positive.
    """
    if length <= 0:
        raise ValueError("Password length must be a positive integer.")

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type (uppercase, lowercase, digits, symbols) must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator Examples:")
    try:
        # Default password (12 chars, all types)
        print(f"Default password: {generate_password()}")

        # 16-character password with letters and digits only
        print(f"Letters & digits (16 chars): {generate_password(length=16, use_symbols=False)}")

        # 8-character password with only lowercase letters
        print(f"Lowercase only (8 chars): {generate_password(length=8, use_uppercase=False, use_digits=False, use_symbols=False)}")

        # 10-character password with all types
        print(f"Strong password (10 chars): {generate_password(length=10, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True)}")

        # Example of error handling
        # print(f"Invalid length: {generate_password(length=0)}")
        # print(f"No character types: {generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=False)}")

    except ValueError as e:
        print(f"Error: {e}")
