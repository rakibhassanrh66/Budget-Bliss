import matplotlib.pyplot as plt

class Dashboard:
    """Handles dashboard display and visualization."""

    @staticmethod
    def display_dashboard(finances):
        """Display the financial dashboard."""
        days_remaining = 31 - len(set([exp['date'][:10] for exp in finances.expenses]))
        daily_limit = finances.calculate_daily_limit(days_remaining)

        print("\n===== Financial Dashboard =====")
        print(f"Budget: {finances.budget} Taka")
        print(f"Total Spent: {finances.total_spent} Taka")
        print(f"Total Deposits: {finances.total_deposits} Taka")
        print(f"Current Balance: {finances.current_balance} Taka")
        print(f"Remaining Days: {days_remaining}")
        print(f"Daily Spending Limit: {daily_limit:.2f} Taka")
        print(f"Rate of Waste: {finances.get_waste_rate():.2f}%")

    @staticmethod
    def display_graph(finances):
        """Provide options to display various financial graphs."""
        while True:
            print("\nGraph Options:")
            print("1. Overall Financial Overview (Balance vs Spent)")
            print("2. Expense by Categories (Pie Chart)")
            print("3. Loan Dues (Bar Chart)")
            print("4. All Graphs (Expenses, Loans, Waste Rate, Remaining Balance)")
            print("5. Exit Graphs")

            choice = input("Choose an option: ")

            if choice == "1":
                Dashboard._overall_financial_overview(finances)
            elif choice == "2":
                Dashboard._expense_by_categories(finances)
            elif choice == "3":
                Dashboard._loan_dues(finances)
            elif choice == "4":
                Dashboard._all_graphs(finances)
            elif choice == "5":
                print("Exiting graphs...")
                break
            else:
                print("Invalid choice, please try again.")

    @staticmethod
    def _overall_financial_overview(finances):
        """Display a bar chart for current balance and total spent."""
        labels = ['Current Balance', 'Total Spent']
        values = [finances.current_balance, finances.total_spent]

        plt.bar(labels, values, color=['green', 'red'])
        plt.title("Financial Overview")
        plt.ylabel("Amount (Taka)")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def _expense_by_categories(finances):
        """Display a pie chart for expenses by category."""
        category_totals = finances.get_category_totals()
        categories = list(category_totals.keys())
        expenses = list(category_totals.values())

        plt.pie(expenses, labels=categories, autopct="%.1f%%", startangle=140)
        plt.title("Expenses by Category")
        plt.axis('equal')
        plt.show()

    @staticmethod
    def _loan_dues(finances):
        """Display a bar chart for loans and due dates."""
        loans = finances.get_loan_due_dates()
        lenders = [loan['lender'] for loan in loans]
        amounts = [loan['amount'] for loan in loans]

        plt.bar(lenders, amounts, color='blue')
        plt.title("Loan Dues")
        plt.xlabel("Lenders")
        plt.ylabel("Loan Amount (Taka)")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def _rate_of_waste(finances):
        """Display a bar chart for the waste rate."""
        labels = ['Waste Rate']
        values = [finances.get_waste_rate()]

        plt.bar(labels, values, color='orange')
        plt.title("Rate of Waste")
        plt.ylabel("Percentage (%)")
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def _remaining_budget(finances):
        """Display a pie chart for remaining budget."""
        remaining = finances.current_balance
        spent = finances.total_spent
        labels = ['Remaining Balance', 'Total Spent']
        values = [remaining, spent]

        plt.pie(values, labels=labels, autopct="%.1f%%", startangle=140)
        plt.title("Remaining Budget vs. Spent")
        plt.axis('equal')
        plt.show()

    @staticmethod
    def _all_graphs(finances):
        """Display all graphs: Expenses, Loans, Waste Rate, Remaining Budget."""
        # Show Overall Financial Overview (Balance vs Spent)
        Dashboard._overall_financial_overview(finances)

        # Show Expense by Categories (Pie Chart)
        Dashboard._expense_by_categories(finances)

        # Show Loan Dues (Bar Chart)
        Dashboard._loan_dues(finances)

        # Show Rate of Waste (Bar Chart)
        Dashboard._rate_of_waste(finances)

        # Show Remaining Budget vs Spent (Pie Chart)
        Dashboard._remaining_budget(finances)
