"""main.py - menu and user interaction. Run this file to start the app."""

import storage
import tracker


def show_menu():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Add Income")
    print("7. Total Income")
    print("8. Edit Income")
    print("9. Show Balance")
    print("10. Category-wise Analysis")
    print("11. Monthly Expense Report")
    print("12. Exit")


def print_expense(expense):
    print("Amount: ₹", expense[0])
    print("Category:", expense[1])
    print("Description:", expense[2])
    print("Date and Time:", expense[3])


# ---------- Menu handlers ----------

def handle_add_expense(expenses, income):
    try:
        amount = float(input("Enter expense amount: ₹"))
        if not tracker.is_valid_amount(amount):
            print("Amount must be a positive number!")
            return
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty!")
            return
        description = input("Enter description: ").strip()
        if not description:
            print("Description cannot be empty!")
            return

        tracker.add_expense(expenses, amount, category, description)
        storage.save_data(expenses, income)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def handle_view_expenses(expenses, income):
    print("\n----- YOUR EXPENSES -----")
    if not expenses:
        print("No expenses recorded yet.")
        return
    for expense in expenses:
        print_expense(expense)
        print("-------------------------")


def handle_total_expenses(expenses, income):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("Total Expenses: ₹", tracker.total_expenses(expenses))


def handle_delete_expense(expenses, income):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n----- YOUR EXPENSES -----")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: ₹{expense[0]}, "
              f"Category: {expense[1]}, "
              f"Description: {expense[2]}, "
              f"Date: {expense[3]}")
    try:
        index = int(input(
            f"Enter the number of the expense to delete (1-{len(expenses)}): "
        )) - 1
        if 0 <= index < len(expenses):
            deleted = tracker.delete_expense(expenses, index)
            storage.save_data(expenses, income)
            print("Deleted Expense:")
            print_expense(deleted)
            print("~~~~~ EXPENSE DELETED SUCCESSFULLY! ~~~~~")
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def handle_edit_expense(expenses, income):
    if not expenses:
        print("No expenses to edit.")
        return

    print("\n----- YOUR EXPENSES -----")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Amount: ₹{expense[0]}, "
              f"Category: {expense[1]}, "
              f"Description: {expense[2]}")
    try:
        n = int(input("Enter expense number to edit: "))
        if not 1 <= n <= len(expenses):
            print("Invalid expense number.")
            return

        print("Leave a field blank to keep its current value.")
        amount = input("Enter new amount: ₹").strip()
        category = input("Enter new category: ").strip()
        description = input("Enter new description: ").strip()

        # Validate before making any changes
        new_amount = None
        if amount:
            new_amount = float(amount)
            if not tracker.is_valid_amount(new_amount):
                print("Amount must be a positive number.")
                return

        tracker.edit_expense(expenses, n - 1, new_amount, category, description)
        storage.save_data(expenses, income)
        print("Expense updated successfully!")
    except ValueError:
        print("Invalid input! Please enter valid values.")


def handle_add_income(expenses, income):
    try:
        amount = float(input("Enter income amount: ₹"))
        if not tracker.is_valid_amount(amount):
            print("Amount must be a positive number!")
            return
        tracker.add_income(income, amount)
        storage.save_data(expenses, income)
        print("Income added successfully!")
        print("Total Income : ₹", tracker.total_income(income))
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def handle_total_income(expenses, income):
    if not income:
        print("No income recorded yet.")
    else:
        print("Total Income : ₹", tracker.total_income(income))


def handle_edit_income(expenses, income):
    if not income:
        print("No income recorded yet.")
        return

    print("\n----- YOUR INCOME -----")
    for i, amount in enumerate(income, start=1):
        print(f"{i}. ₹{amount}")
    try:
        index = int(input(
            f"Enter the number of the income to edit (1-{len(income)}): "
        )) - 1
        if not 0 <= index < len(income):
            print("Invalid income number!")
            return

        new_amount = float(input("Enter the new income amount: ₹"))
        if not tracker.is_valid_amount(new_amount):
            print("Amount must be a positive number!")
            return

        tracker.edit_income(income, index, new_amount)
        storage.save_data(expenses, income)
        print("Income updated successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


def handle_balance(expenses, income):
    if not income and not expenses:
        print("No income or expenses recorded yet.")
        return

    total_income, total_expenses, balance = tracker.calculate_balance(income, expenses)
    print("\n----- FINANCIAL SUMMARY -----")
    print("Total Income: ₹", total_income)
    print("Total Expenses: ₹", total_expenses)
    print("Balance: ₹", balance)
    if balance < 0:
        print("Warning:Expenses exceed Income! Consider reviewing your expenses.")
    elif balance == 0:
        print("You have balanced your income and expenses.")
    else:
        print("You have a positive balance. Good job on managing your finances!")


def handle_category_analysis(expenses, income):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n-------CATEGORY-WISE ANALYSIS-------")
    for category, total in tracker.category_totals(expenses).items():
        print(category, ": ₹", total)


def handle_monthly_report(expenses, income):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n----- MONTHLY EXPENSE REPORT -----")
    for month_year, total in tracker.monthly_totals(expenses):
        print(month_year, ": ₹", total)


# Maps each menu choice to its handler function
HANDLERS = {
    "1": handle_add_expense,
    "2": handle_view_expenses,
    "3": handle_total_expenses,
    "4": handle_delete_expense,
    "5": handle_edit_expense,
    "6": handle_add_income,
    "7": handle_total_income,
    "8": handle_edit_income,
    "9": handle_balance,
    "10": handle_category_analysis,
    "11": handle_monthly_report,
}


def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("     PERSONAL EXPENSE TRACKER     ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    expenses, income = storage.load_data()

    while True:
        show_menu()
        choice = input("Enter your choice (1-12): ")

        if choice == "12":
            print("Thank you for using the Personal Expense Tracker!    Exiting...")
            break
        handler = HANDLERS.get(choice)
        if handler:
            handler(expenses, income)
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
