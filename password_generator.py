"""
🔐 Password Generator Script
Author: Japinder Kaur
--------------------------------------------
This script generates strong, random passwords using
uppercase, lowercase, digits, and special symbols.

🪄 Usage:
    Run the script and enter the desired password length.
    Example:
        Enter password length: 12
        Generated Password: aB3#tP8@qK!z
"""

import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length.
    Includes uppercase, lowercase, digits, and special symbols.
    """
    # All possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Validate length
    if length < 4:
        return "❌ Password length must be at least 4 for better security."

    # Randomly generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    try:
        # Take user input
        length = int(input("Enter password length: "))
        # Generate and display password
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("❌ Please enter a valid number.")
