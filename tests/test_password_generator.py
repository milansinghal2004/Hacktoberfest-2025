"""
Test cases:
- Default password (12 chars, all types)
- 10-character password with symbols
- 10-character password with all types
- Error handling: length <= 0, no character types selected
"""
import string
from scripts.password_generator import generate_password


def test_generate_password_default():
    default_password = generate_password()
    assert len(default_password) == 12
    assert any(char.isupper() for char in default_password)
    assert any(char.islower() for char in default_password)
    assert any(char.isdigit() for char in default_password)
    assert any(char in string.punctuation for char in default_password)


def test_generate_password_all_false():
    password = generate_password(
        length=10,
        use_uppercase=False,
        use_lowercase=False,
        use_digits=False,
        use_symbols=True,
    )
    assert len(password) == 10
    assert not any(char.isupper() for char in password)
    assert not any(char.islower() for char in password)
    assert not any(char.isdigit() for char in password)


def test_generate_password_all_true():
    password = generate_password(
        length=10,
        use_uppercase=True,
        use_lowercase=True,
        use_digits=True,
        use_symbols=True,
    )
    assert len(password) == 10
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)


def test_generate_password_error_handling():
    try:
        generate_password(length=0)
    except ValueError as e:
        assert str(e) == "Password length must be a positive integer."
    try:
        generate_password(
            use_uppercase=False,
            use_lowercase=False,
            use_digits=False,
            use_symbols=False,
        )
    except ValueError as e:
        assert str(e) == (
            "At least one character type "
            "(uppercase, lowercase, digits, symbols) "
            "must be selected."
        )
