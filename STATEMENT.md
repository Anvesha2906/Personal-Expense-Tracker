# Project Statement: Personal Expense Tracker

## Problem Statement

Many people struggle to keep track of where their money goes. Notes in a phone or memory-based budgeting make it hard to know how much was spent, on what, and whether spending is within income. Spreadsheets and finance apps can feel complicated or heavy for someone who only wants a simple, private way to record daily spending.

## Objective

To build a lightweight, command-line **Personal Expense Tracker** in Python that lets a user record income and expenses, review them, and understand their spending habits, with all data stored locally and persistently.

## Scope

**In scope**

- Recording, viewing, editing and deleting expenses (amount, category, description, timestamp)
- Recording, viewing and editing income
- Calculating total income, total expenses and current balance
- Analysing spending by category and by month
- Saving data to a local file so it persists between sessions
- Validating user input and handling a corrupted data file safely

**Out of scope (current version)**

- Graphical or web interface
- Multiple users or password protection
- Cloud sync or bank integration
- Income dates/sources and monthly income reports
- Exporting reports to CSV or PDF

## Proposed Solution

A menu-driven console application with 12 options. The program runs in a loop until the user exits, loads existing data from `tracker.txt` at startup, and saves after every change. Expenses are stored as lists of `[amount, category, description, date_time]` and income as a list of amounts, serialised as JSON.

## Key Features

| # | Feature | Purpose |
|---|---------|---------|
| 1 | Add Expense | Record a new expense with auto date and time |
| 2 | View Expenses | List all recorded expenses |
| 3 | Total Expenses | Show the sum of all expenses |
| 4 | Delete Expense | Remove a wrongly entered expense |
| 5 | Edit Expense | Correct amount, category or description |
| 6 | Add Income | Record salary or extra income |
| 7 | Total Income | Show the sum of all income |
| 8 | Edit Income | Correct an income entry |
| 9 | Show Balance | Income minus expenses, with a status message |
| 10 | Category-wise Analysis | See spending per category |
| 11 | Monthly Expense Report | See spending per month |
| 12 | Exit | Close the program |

## Technology Used

- **Language:** Python 3
- **Libraries:** `json`, `datetime`, `math` (standard library only)
- **Storage:** Local JSON file (`tracker.txt`)
- **Interface:** Command line

## Programming Concepts Demonstrated

- Loops and conditional statements
- Lists, dictionaries and list comprehensions/generators
- File handling and JSON serialisation
- Exception handling (`ValueError`, `FileNotFoundError`, `JSONDecodeError`)
- Input validation
- Date and time formatting and parsing
- Sorting with a key function
  
## Targeted Audiences

The primary targeted audience for this project includes:
- College students who want to keep track of their daily spending and available balance.
- Young individuals who are beginning to manage their personal finances.
- Users with simple financial-recording needs who prefer a lightweight application instead of a complex financial-management system.
- Python beginners and students who want to understand how programming concepts can be applied to a real-world problem.

## Expected Outcome

A working tool that gives the user a clear picture of their finances: what they earn, what they spend, where the money goes, and how much is left, without needing any external software or internet connection.

## Limitations

- Command-line only, with no charts or visuals
- Income entries have no date or source
- Expense dates cannot be edited
- Amounts stored as floats may show small rounding differences
- Single-user, unencrypted local storage

## Future Enhancements

- Refactor the code into functions and store expenses as dictionaries
- Add dates and sources to income for monthly income vs. expense reports
- Confirmation prompt before deleting
- Export reports to CSV
- Search and filter by date range or category
- Budget limits per category with alerts
- A graphical or web interface

## Conclusion

The Personal Expense Tracker solves the everyday problem of tracking money in a simple, private and easy-to-use way. It also serves as a solid foundation for adding more advanced features in the future.
