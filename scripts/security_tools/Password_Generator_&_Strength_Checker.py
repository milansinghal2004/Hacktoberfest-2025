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



class PasswordValidator:
    """
    Analyzes the strength of a password based on common security criteria.
    """

    @staticmethod
    def check_strength(password: str) -> dict:
        score = 0
        feedback = []

        # Length check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Password is too short (min 8 characters).")

        # Character variety checks
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Missing uppercase letters.")

        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Missing lowercase letters.")

        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Missing digits.")

        if any(c in string.punctuation for c in password):
            score += 1
        else:
            feedback.append("Missing special characters.")

        # Mapping score to strength
        strength_map = {
            0: "Very Weak",
            1: "Weak",
            2: "Medium",
            3: "Strong",
            4: "Very Strong",
            5: "Excellent",
            6: "Excellent"
        }

        return {
            "score": score,
            "strength": strength_map.get(score, "Very Weak"),
            "feedback": feedback
        }


def main():
    print("-" * 30)
    print("Secure Password Tool")
    print("-" * 30)

    while True:
        print("\nMenu:")
        print("1. Generate a New Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nSelect an option (1-3): ").strip()

        if choice == '1':
            try:
                length = input("Enter password length (default 16): ").strip()
                length = int(length) if length else 16
                gen = PasswordGenerator(length=length)
                password = gen.generate()
                print(f"\n[+] Generated Password: {password}")
                
                # Automatically show strength for generated password
                strength = PasswordValidator.check_strength(password)
                print(f"    Strength: {strength['strength']}")
            except ValueError as e:
                print(f"[-] Error: {e}")

        elif choice == '2':
            pwd = input("Enter password to check: ").strip()
            if not pwd:
                print("[-] Password cannot be empty.")
                continue
            
            result = PasswordValidator.check_strength(pwd)
            print(f"\nStrength: {result['strength']} (Score: {result['score']}/6)")
            if result['feedback']:
                print("Feedback:")
                for item in result['feedback']:
                    print(f" - {item}")

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("[-] Invalid option. Please try again.")


if __name__ == "__main__":
    main()
