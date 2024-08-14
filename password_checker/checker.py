import re


def check_password_strength(password):
    # Initialize strength score
    strength = 0

    # Check length first
    if len(password) < 8:
        return "weak"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        print("Password must contain at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("Password must contain at least one uppercase letter.")

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        print("Password must contain at least one digit.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        print("Password must contain at least one special character.")

    # Print the password strength
    if strength == 4:
        return "strong"
    elif 2 <= strength < 4:
        return "medium"
    else:
        return "weak"
