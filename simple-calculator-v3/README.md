# Python Projects

## Simple Python Calculator

**Version 3.0**

A beginner-friendly command-line calculator built with Python, featuring improved input validation and exception handling.

### Features

- Addition, subtraction, multiplication, and division
- Supports decimal, negative, and zero values
- Validates numeric input using `try/except ValueError`
- Accepts only supported arithmetic operators (`+`, `-`, `*`, `/`)
- Handles division by zero using `try/except ZeroDivisionError`
- Displays helpful error messages without crashing on invalid numeric input or division by zero
- Repeatedly prompts for valid input when necessary
- Allows multiple calculations in one session
- Validates case-insensitive continue/exit responses (`y` or `n`)
- Uses separate input, arithmetic, and main functions for readability and maintainability

### Requirements

- Python 3
- No external dependencies

### How to Run

Open a terminal in the project directory and run:

```bash
python calculator.py
```

### Example Usage

```text
Enter first number: abc
Invalid input! Please enter a number.

Enter first number: 10
Enter second number: 5
Enter operator (+, -, *, /): +
Result: 15.0

Again (y/n)? n
Goodbye!
```

### Testing

All 24 planned manual test cases passed:

| Test category | Passed |
| --- | ---: |
| Normal calculations | 7/7 |
| Invalid input and error handling | 9/9 |
| Edge cases and program flow | 8/8 |
| **Total** | **24/24** |

### Project Status

- **Version 1.0** — Initial working calculator with basic arithmetic and repeated calculations.
- **Version 2.0** — Completed input validation, exception handling, code refactoring, and manual testing.

### Planned Improvements

Proposed enhancements for Version 3.0:

- Add type hints and function docstrings
- Simplify operator selection using a dictionary and function references
- Improve numeric validation by rejecting non-finite values (`nan` and `inf`)
- Organize functions into separate modules
- Implement automated unit tests using `unittest`
- Add calculation history
- Save calculation history using JSON file handling
