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
        df = pd.DataFrame(self.expenses)
        df.to_csv(file_path, index=False)

    def calculate_daily_limit(self, days_remaining=31):
        if days_remaining <= 0:
            return 0
        return self.current_balance / days_remaining

    def get_category_totals(self):
        """Return total expenses for each category."""
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['expense']
        return category_totals

    def get_waste_rate(self):
        """Calculate the waste rate as the percentage of the total budget spent."""
        if self.budget == 0:
            return 0
        return (self.total_spent / self.budget) * 100

    def get_loan_due_dates(self):
        """Return loan due dates."""
        return self.loans
