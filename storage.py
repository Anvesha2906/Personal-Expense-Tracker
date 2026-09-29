"""storage.py - handles reading and writing the tracker data file."""

import json

DATA_FILE = "tracker.txt"


def load_data():
    """Load expenses and income from the data file.

    Returns (expenses, income). If the file doesn't exist yet, returns two
    empty lists. If the file is corrupted, prints a message and exits so the
    existing file is never overwritten.
    """
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data["expenses"], data["income"]
    except FileNotFoundError:
        return [], []
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Error: The data file is corrupted. Starting with empty data.")
        print("Please restore your data from a backup if available.")
        raise SystemExit


def save_data(expenses, income):
    """Save expenses and income to the data file."""
    data = {
        "expenses": expenses,
        "income": income
    }
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
