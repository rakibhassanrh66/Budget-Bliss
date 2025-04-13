import pandas as pd
from datetime import datetime

class Finances:
    """Handles financial tracking and operations."""

    def __init__(self, budget):
        self.budget = budget
        self.expenses = []
        self.loans = []
        self.total_spent = 0
        self.total_deposits = 0
        self.current_balance = budget

    def add_expense(self, expense, category, description):
        self.expenses.append({
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'expense': expense,
            'category': category,
            'description': description
        })
        self.total_spent += expense
        self.current_balance -= expense

    def add_loan(self, lender_name, amount, return_date):
        self.loans.append({
            'lender': lender_name,
            'amount': amount,
            'date_taken': datetime.now().strftime("%Y-%m-%d"),
            'return_date': return_date
        })
        self.total_deposits += amount
        self.current_balance += amount

    def save_to_csv(self, file_path="assets/finances.csv"):
        # Combine expenses and loans into a single DataFrame
        expenses_df = pd.DataFrame(self.expenses)
        loans_df = pd.DataFrame(self.loans)
        
        # Saving expenses and loans as separate CSV files
        expenses_df.to_csv(file_path, index=False, mode='w')  # Mode 'w' for overwrite
        loans_df.to_csv(file_path, index=False, mode='a')  # Mode 'a' for append
        
        print(f"Data saved to {file_path} successfully.")
        
    def calculate_daily_limit(self, days_remaining=31):
        if days_remaining <= 0:
            return 0
        return self.current_balance / days_remaining
