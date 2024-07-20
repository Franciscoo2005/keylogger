import re
import argparse


def check_password_complexity(password):
    """Check the complexity of the given password and return a report."""

    if len(password) < 8:
        return "Password must be at least 8 characters long."

    checks = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'[0-9]', password) is not None,
        'special_char': re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }

    if not all(checks.values()):
        report = []
        if not checks['length']:
            report.append("Password must be at least 8 characters long.")
        if not checks['uppercase']:
            report.append("Password must include at least one uppercase letter.")
        if not checks['lowercase']:
            report.append("Password must include at least one lowercase letter.")
        if not checks['digit']:
            report.append("Password must include at least one digit.")
        if not checks['special_char']:
            report.append("Password must include at least one special character.")
        return " ".join(report)

    # Check for common patterns (you can add more patterns or use a list of words)
    common_patterns = ['1234', 'password', 'qwerty', 'abc', 'password1']
    if any(pattern in password.lower() for pattern in common_patterns):
        return "Password contains a common pattern or is too weak."

    return "Password is strong."


result = check_password_complexity(input("enter text:"))
print(f"Result: {result}\n")
