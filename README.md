# Password Strength Analyzer

A Python-based Password Strength Analyzer that evaluates password security using common password policies. The application checks password strength, detects commonly used passwords, provides improvement suggestions, generates secure passwords, and saves analysis reports in CSV format.

---

## Features

- Analyze password strength
- Detect common weak passwords
- Calculate password security score
- Suggest improvements
- Generate secure random passwords
- Save reports in CSV format
- Menu-driven console application

---

## Technologies Used

- Python 3.x
- Regular Expressions (re)
- CSV Module
- Random Module
- String Module
- File Handling

---

## Project Structure

password-strength-analyzer/

├── main.py

├── password_checker.py

├── password_generator.py

├── common_passwords.txt

├── report.csv

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

Clone the repository

```bash
git clone https://github.com/sneha-65/password-strength-analyzer.git
```

Move into the project directory

```bash
cd password-strength-analyzer
```

Run the application

```bash
python main.py
```

---

## Menu

```
1. Analyze Password
2. Generate Secure Password
3. Exit
```

---

## Example

### Analyze Password

```
Enter Password

Hello@123
```

Output

```
Password Score: 7/7

Password Strength: Strong
```

---

### Generate Password

```
Enter Password Length

12
```

Output

```
Generated Password

H@7Lm8#QwP2!
```

---

## Password Rules

- Minimum 8 characters
- Uppercase letter
- Lowercase letter
- Number
- Special character

---

## Report

Each password analysis is stored in

```
report.csv
```

Example

| Date | Length | Score | Strength |
|------|--------|-------|----------|
|2026-07-01|10|6|Strong|

---

## Future Improvements

- GUI using Tkinter
- Flask Web Application
- Password Hashing
- SQLite Database
- User Authentication
- Dark Mode Interface
- Password History

---

## Author

Sneha
