import pandas as pd
from datetime import datetime
from data_input import DataInput
from finances import Finances
from dashboard import Dashboard

def main():
    budget = DataInput.get_initial_budget()
    finances = Finances(budget)

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Add Loan")
        print("3. Show Dashboard")
        print("4. Show Graphs")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            expense, category, description = DataInput.get_expense_input()
            finances.add_expense(expense, category, description)
        elif choice == "2":
            lender_name, amount, return_date = DataInput.get_loan_input()
            finances.add_loan(lender_name, amount, return_date)
        elif choice == "3":
            Dashboard.display_dashboard(finances)
        elif choice == "4":
            Dashboard.display_graph(finances)
        elif choice == "5":
            print("Exiting program...")
            finances.save_to_csv()  # Save data to CSV before exiting
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
