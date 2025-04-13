from datetime import datetime

class DataInput:
    """Handles user input for financial data."""

    @staticmethod
    def get_initial_budget():
        while True:
            try:
                budget = float(input("Enter your initial budget (Taka): "))
                if budget <= 0:
                    raise ValueError("Budget must be a positive number.")
                return budget
            except ValueError as e:
                print(e)

    @staticmethod
    def get_expense_input():
        while True:
            try:
                expense = float(input("Enter your expense amount: "))
                if expense <= 0:
                    raise ValueError("Expense must be a positive number.")

                category = input("Enter the category of the expense (e.g., Rent, Food, Bills, Personal, Shopping, Tour, Saving): ").capitalize()
                if category not in ['Rent', 'Food', 'Bills', 'Personal', 'Shopping', 'Tour', 'Saving']:
                    raise ValueError("Invalid category. Choose from Rent, Food, Bills, Personal, Shopping, Tour, or Saving.")

                description = input("Enter a description for the expense: ")
                if not description.strip():
                    raise ValueError("Description cannot be empty.")

                return expense, category, description
            except ValueError as e:
                print(e)

    @staticmethod
    def get_loan_input():
        while True:
            try:
                lender_name = input("Enter lender name: ").strip()
                if not lender_name:
                    raise ValueError("Lender name cannot be empty.")

                amount = float(input("Enter loan amount: "))
                if amount <= 0:
                    raise ValueError("Loan amount must be a positive number.")

                return_date = input("Enter loan return date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(return_date, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Invalid date format. Use YYYY-MM-DD.")

                return lender_name, amount, return_date
            except ValueError as e:
                print(e)
