import string
import secrets


class PasswordGenerator:
    """
    Generates a secure random password using Python's secrets module.
    Beginner‑friendly version with clear structure and example usage.
    """

    def __init__(self, length=16, use_upper=True, use_lower=True,
                 use_digits=True, use_special=True):
        if not isinstance(length, int) or length < 4:
            raise ValueError("Password length must be an integer >= 4")

        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self) -> str:
        """Generate a secure password with the selected options."""
        charset = ""
        if self.use_upper:
            charset += string.ascii_uppercase
        if self.use_lower:
            charset += string.ascii_lowercase
        if self.use_digits:
            charset += string.digits
        if self.use_special:
            charset += string.punctuation

        if not charset:
            raise ValueError("Please select at least one character type.")

        # Ensure at least one from each selected type
        password = []
        if self.use_upper:
            password.append(secrets.choice(string.ascii_uppercase))
        if self.use_lower:
            password.append(secrets.choice(string.ascii_lowercase))
        if self.use_digits:
            password.append(secrets.choice(string.digits))
        if self.use_special:
            password.append(secrets.choice(string.punctuation))

        # Fill remaining length securely
        remaining = self.length - len(password)
        password += [secrets.choice(charset) for _ in range(remaining)]

        # Shuffle for randomness
        secrets.SystemRandom().shuffle(password)
        return "".join(password)


# Example usage
if __name__ == "__main__":
    gen = PasswordGenerator(length=12)
    print("Generated Password:", gen.generate())
