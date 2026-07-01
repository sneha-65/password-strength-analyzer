# password_checker.py

import re
import csv
import os
from datetime import datetime


def check_password_strength(password):
    """
    Checks different password security rules.
    Returns a dictionary containing True/False values.
    """

    result = {
        "Length": len(password) >= 8,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Special Character": bool(re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|`~]", password))
    }

    return result


def check_common_password(password):
    """
    Checks whether the password exists in common_passwords.txt
    """

    filename = "common_passwords.txt"

    if not os.path.exists(filename):
        return False

    with open(filename, "r") as file:
        common_passwords = [line.strip().lower() for line in file]

    return password.lower() in common_passwords


def password_score(result):
    """
    Calculates password score out of 7.
    """

    score = 0

    if result["Length"]:
        score += 2

    if result["Uppercase"]:
        score += 1

    if result["Lowercase"]:
        score += 1

    if result["Number"]:
        score += 1

    if result["Special Character"]:
        score += 2

    return score


def generate_suggestions(result):
    """
    Returns suggestions to improve password.
    """

    suggestions = []

    if not result["Length"]:
        suggestions.append("Use at least 8 characters.")

    if not result["Uppercase"]:
        suggestions.append("Add an uppercase letter.")

    if not result["Lowercase"]:
        suggestions.append("Add a lowercase letter.")

    if not result["Number"]:
        suggestions.append("Include at least one number.")

    if not result["Special Character"]:
        suggestions.append("Include a special character.")

    return suggestions


def save_report(password, score, strength):
    """
    Saves password analysis to report.csv
    """

    filename = "report.csv"

    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Password_Length",
                "Score",
                "Strength"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            len(password),
            score,
            strength
        ])