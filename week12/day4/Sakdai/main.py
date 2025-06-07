import os
from libraries import *

# File to store expenses
FILE_NAME = "expenses.csv"

def main():

    if os.path.exists('expenses.csv') == False:
        initialize_csv(FILE_NAME)

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Transport): ")
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            add_expense(FILE_NAME, category, description, amount)

        elif choice == "2":
            view_expenses(FILE_NAME)

        elif choice == "3":
            calculate_total(FILE_NAME)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()