import random
import string


def generate_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    # Ensure at least one character from each pool
    all_chars = letters + digits + special_chars
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the rest of the password
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    try:
        length = int(input("Enter the password length (minimum 6): "))
        print(f"Generated Password: {generate_password(length)}")
    except ValueError as e:
        print(e)