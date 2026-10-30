# Expense Tracker

A Python project for recording personal expenses, organizing them into categories, and calculating spending totals using CSV file storage.

## About the Project

This project was developed as part of my academic programming practice. It focuses on managing personal expenses through a simple command-line application.

The program allows users to register expenses by entering a description, category, amount, and date. The information is stored in a CSV file so that expenses can be accessed again when the program is executed.

## Features

- Register personal expenses.
- Assign categories to each expense.
- Enter the expense description, amount, and date.
- Display all registered expenses.
- Calculate the total amount spent.
- Calculate spending totals by category.
- Save expense records in a CSV file.
- Load previously saved expenses when starting the program.
- Validate user input, including amounts and dates.

## Technologies and Concepts

- **Language:** Python
- **Libraries:** `csv`, `os`, and `datetime`
- **File handling:** Reading and writing CSV files.
- **Data structures:** Lists and dictionaries.
- **Functions:** Organizing the program into reusable functions.
- **Data validation:** Checking user input and numeric values.
- **Date handling:** Working with dates using Python's `datetime` module.

## Project Structure

```text
expense-tracker/
├── main.py
├── README.md
└── expenses.csv (created automatically)
```

## Requirements

- Python 3
- No external libraries required.

The `main.py` file contains the main program. The `expenses.csv` file is created automatically when the first expense is registered.

## How to Run

### 1. Open a terminal

Navigate to the directory containing the Python file.

### 2. Run the program

```bash
python main.py
```

### 3. Use the menu

Select an option to register expenses, display records, calculate the total spent, or review expenses by category.

**Note:** Expense information is saved automatically in `expenses.csv`. The file is stored in the program's working directory.

## What I Learned

While working on this project, I practiced creating functions, organizing information with lists and dictionaries, handling CSV files, validating user input, working with dates, and calculating totals using Python.

## Author

**Fátima Montoya**  
Information Systems Engineering Student
