import sys
import os

# Add parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from password_checker import check_password_strength


def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        # Prompt the user to enter a password
        password = input(
            "Enter a password to check its strength (or type 'exit' to quit): "
        )

        # Check if the user wants to exit
        if password.lower() == "exit":
            print("Exiting the Password Strength Checker. Goodbye!")
            break

        # Check the strength of the password
        strength = check_password_strength(password)

        # Display the result
        print(f"Password strength: {strength}\n")


if __name__ == "__main__":
    main()
