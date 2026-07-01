# password_generator.py

import random
import string


def generate_password(length):
    """
    Generates a secure random password.
    """

    if length < 8:
        raise ValueError("Password length must be at least 8.")

    # Character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_=+"

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Remaining characters
    all_characters = uppercase + lowercase + digits + special

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle to randomize positions
    random.shuffle(password)

    return "".join(password)