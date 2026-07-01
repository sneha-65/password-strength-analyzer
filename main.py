# main.py

from password_checker import (
    check_password_strength,
    check_common_password,
    password_score,
    generate_suggestions,
    save_report
)

from password_generator import generate_password


def menu():
    while True:
        print("\n" + "=" * 45)
        print("      PASSWORD STRENGTH ANALYZER")
        print("=" * 45)
        print("1. Analyze Password")
        print("2. Generate Secure Password")
        print("3. Exit")
        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":

            password = input("\nEnter Password: ")

            # Check if common password
            if check_common_password(password):
                print("\nWARNING: This is a commonly used password!")

            # Check strength
            result = check_password_strength(password)

            print("\nPassword Analysis")
            print("-" * 30)

            for key, value in result.items():
                print(f"{key:<20}: {'Yes' if value else 'No'}")

            score = password_score(result)

            print("\nPassword Score:", score, "/7")

            if score <= 3:
                strength = "Weak"
            elif score <= 5:
                strength = "Medium"
            else:
                strength = "Strong"

            print("Password Strength:", strength)

            suggestions = generate_suggestions(result)

            if suggestions:
                print("\nSuggestions:")
                for suggestion in suggestions:
                    print("-", suggestion)

            save_report(password, score, strength)

        elif choice == "2":

            length = input("Enter password length (minimum 8): ")

            if not length.isdigit():
                print("Please enter a valid number.")
                continue

            length = int(length)

            if length < 8:
                print("Password length must be at least 8.")
                continue

            password = generate_password(length)

            print("\nGenerated Secure Password:")
            print(password)

        elif choice == "3":
            print("\nThank you for using Password Strength Analyzer.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()