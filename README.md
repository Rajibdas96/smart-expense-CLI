# smart expense CLI

A simple command-line expense tracker built with Python.

This project allows users to add, view, search, edit, and delete expenses directly from the terminal. Expenses are stored locally in a JSON file so the data remains available after the program is closed.

## Features

* Add new expenses
* View all expenses
* Search expenses
* Edit existing expenses
* Delete expenses
* Categorize expenses
* Calculate total expenses
* Store data locally using JSON
* Basic input validation
* Simple command-line interface

## Technologies Used

* Python
* JSON
* File Handling
* Functions
* Lists and Dictionaries
* Exception Handling

## Project Structure

```text
smart expense CLI/
│
├── main.py
├── user_storage.json
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Rajibdas96/smart-expense-CLI
```

### 2. Open the project folder

```bash
cd smart expense CLI
```

### 3. Run the program

```bash
python main.py
```

## Example

After starting the program, you will see a menu similar to:

```text
==============================
      EXPENSE TRACKER
==============================

1. Add Expense
2. View Expenses
3. Search Expense
4. Edit Expense
5. Delete Expense
6. Show Total
7. Exit

Enter your choice:
```

Example expense:

```text
Amount: 150
Category: Food
Description: Lunch
```

The program stores the information in `user_storage.json`.

## Example Output

```text
ID: 1
Amount: ₹150
Category: Food
Description: Lunch

ID: 2
Amount: ₹50
Category: Transport
Description: Bus
```

Total:

```text
Total Expenses: ₹200
```

## What I Learned

While building this project, I practiced:

* Writing Python functions
* Working with lists and dictionaries
* Reading and writing JSON files
* Handling user input
* Validating data
* Using exceptions
* Organizing a small Python project
* Building a complete program from start to finish

## Future Improvements

Some features I may add later:

* Monthly expense reports
* Expense charts
* CSV export
* Date-based filtering
* Budget limits
* SQLite database
* Better command-line interface
* Unit tests

## Project Status

**Version:** 1.0

This is a learning project and will be improved as I continue developing my Python skills.

## Author

**Rajib**

This project is part of my journey of learning Python by building real projects instead of only following tutorials.
