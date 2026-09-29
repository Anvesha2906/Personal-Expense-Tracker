"""tracker.py - core logic for expenses, income and reports.

Nothing in this module reads input or prints anything, so every function
can be tested on its own. An expense is stored as:
    [amount, category, description, "DD-MM-YYYY HH:MM:SS"]
Income is stored as a plain list of amounts.
"""

import math
from datetime import datetime

DATE_FORMAT = "%d-%m-%Y %H:%M:%S"


# ---------- Validation ----------

def is_valid_amount(amount):
    """An amount must be a finite number greater than zero."""
    return math.isfinite(amount) and amount > 0


# ---------- Expenses ----------

def add_expense(expenses, amount, category, description):
    """Create an expense with the current date and time and add it."""
    date_time = datetime.now().strftime(DATE_FORMAT)
    expense = [amount, category, description, date_time]
    expenses.append(expense)
    return expense


def edit_expense(expenses, index, amount=None, category=None, description=None):
    """Update only the fields that are given (not None / not empty)."""
    expense = expenses[index]
    if amount is not None:
        expense[0] = amount
    if category:
        expense[1] = category
    if description:
        expense[2] = description
    return expense


def delete_expense(expenses, index):
    """Remove and return the expense at the given index."""
    return expenses.pop(index)


def total_expenses(expenses):
    return sum(expense[0] for expense in expenses)


# ---------- Income ----------

def add_income(income, amount):
    income.append(amount)


def edit_income(income, index, new_amount):
    income[index] = new_amount


def total_income(income):
    return sum(income)


# ---------- Balance and reports ----------

def calculate_balance(income, expenses):
    """Return (total_income, total_expenses, balance)."""
    inc = total_income(income)
    exp = total_expenses(expenses)
    return inc, exp, inc - exp


def category_totals(expenses):
    """Return {category: total}. Categories are grouped case-insensitively."""
    totals = {}
    for expense in expenses:
        category = expense[1].strip().title()
        totals[category] = totals.get(category, 0) + expense[0]
    return totals


def monthly_totals(expenses):
    """Return [("Month Year", total), ...] sorted from oldest to newest."""
    totals = {}
    for expense in expenses:
        date_time = datetime.strptime(expense[3], DATE_FORMAT)
        month_start = date_time.replace(day=1, hour=0, minute=0, second=0)
        totals[month_start] = totals.get(month_start, 0) + expense[0]
    return [(month.strftime("%B %Y"), total)
            for month, total in sorted(totals.items())]
