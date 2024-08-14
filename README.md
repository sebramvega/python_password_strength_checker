# Password Strength Checker

This is a Python package that checks the strength of a password based on various criteria.

## Features

- Ensures the password is at least 8 characters long.
- Checks for the presence of lowercase letters.
- Checks for the presence of uppercase letters.
- Checks for the presence of digits.
- Checks for the presence of special characters.

## Usage

### Running the Password Checker with User Input

1. Clone the repository or download the files.
2. Navigate to the `scripts` directory.
3. Run the password checker script.

```bash
python run_checker.py
```

4. Enter a password when promtped which will be evaluated by the script according to some criteria. Type 'exit' to quit.

**OR**

1. Run the tests using `unittest`:

```bash
python -m unittest discover -s tests
```

## How it Works

The _check_password_strength_ function evalueates the strength of a password based on the following criteria:

    - **Length**: The password must be at least 8 characters long. If it is shorter, it is automatically rated as "weak."
    - **Lowercase Letters**: The password should contain at least one lowercase letter.
    - **Uppercase Letters**: The password should contain at least one uppercase letter.
    - **Digits**: The password should contain at least one digit.
    - **Special Characters**: The password should contain at least one special character.

# Strength Levels

    - **Strong**: The password meets all criteria.
    - **Medium**: The password meets 2 or 3 criterias.
    - **Weak**: The password meets fewer than 2 criteria, or it is shorter than 8 characters.

### License

This project is open-source and available under the **MIT License**.
