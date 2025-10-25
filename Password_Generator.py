import random
import string

def generate_password(length):
    # Characters to include: letters, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Taking input from user
length = int(input("Enter password length: "))

# Generate and display password
print("Generated Password:", generate_password(length))
