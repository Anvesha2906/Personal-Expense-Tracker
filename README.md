# Personal Expense Tracker

A simple, menu-driven command-line app written in Python to track your income and expenses in ₹. Data is saved automatically to a local JSON file, so nothing is lost between runs.

## Features

- **Add, view, edit and delete expenses** (amount, category, description, auto-stamped date and time)
- **Add, view and edit income**
- **Total expenses** and **total income** at a glance
- **Balance summary** with a warning when expenses exceed income
- **Category-wise analysis** showing how much you spent per category (case-insensitive, so `food` and `Food` are grouped together)
- **Monthly expense report** sorted chronologically
- **Input validation** for invalid numbers, negative or zero amounts, `nan`/`inf` (in most options), and empty fields
- **Corrupted-file protection**: if the data file can't be read, the program stops instead of overwriting your data

## Requirements

- Python 3.6 or newer
- No external libraries (uses only `json`, `datetime` and `math` from the standard library)

## Getting Started

1. Save the script as `expense_tracker.py` (or any name you like).
2. Open a terminal in the same folder.
3. Run:

   ```bash
   python expense_tracker.py
   ```

On first run, a `tracker.txt` file is created automatically in the same folder the first time you save something.

## Menu

| Option | Action |
|--------|--------|
| 1 | Add Expense |
| 2 | View Expenses |
| 3 | Total Expenses |
| 4 | Delete Expense |
| 5 | Edit Expense (leave a field blank to keep its current value) |
| 6 | Add Income |
| 7 | Total Income |
| 8 | Edit Income |
| 9 | Show Balance |
| 10 | Category-wise Analysis |
| 11 | Monthly Expense Report |
| 12 | Exit |

## Example

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     PERSONAL EXPENSE TRACKER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Add Expense
...
Enter your choice (1-12): 1
Enter expense amount: ₹250
Enter category: Food
Enter description: Lunch with friends
Expense added successfully!
```

## Data Storage

All data lives in `tracker.txt` (JSON format) next to the script:

```json
{
    "expenses": [
        [250.0, "Food", "Lunch with friends", "29-09-2026 13:45:10"]
    ],
    "income": [
        20000.0
    ]
}
```

- Each **expense** is stored as `[amount, category, description, "DD-MM-YYYY HH:MM:SS"]`.
- **Income** is stored as a plain list of amounts.

**Tip:** Back up `tracker.txt` regularly. If the file becomes corrupted, the app will show an error and exit without touching it, so you can restore from a backup.

## Project Structure

```
.
├── expense_tracker.py   # Main program
├── tracker.txt          # Auto-generated data file
└── README.md
```

## Known Limitations

- Income entries have no date or source, so there is no monthly income report.
- The expense date can't be edited after creation.
- Amounts are stored as floats, which can occasionally cause tiny rounding differences.

## Future Improvements

- Split the code into functions
- Store expenses as dictionaries instead of lists
- Add dates and sources to income
- Confirmation prompt before deleting
- Export reports to CSV
- Search and filter by date range or category

## License

This project is free to use and modify for personal and learning purposes.
