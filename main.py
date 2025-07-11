import sys
from data_management import DataManagement
from data_analysis import DataAnalysis
from visualization import DataVisualization
from budget_management import BudgetManagement
from menu_screen import MenuScreen

class PersonalFinanceTracker:
    def __init__(self):
        self.data_management = DataManagement()
        self.data_analysis = DataAnalysis(self.data_management.transactions)
        self.budget_management = BudgetManagement(self.data_management.transactions)
        self.visualization = DataVisualization(self.data_management.transactions, self.budget_management.spends_and_budget)
        self.menu_screen = MenuScreen(
            top_message="=== Personal Finance Tracker ===",
            exit_message="Exiting the Personal Finance Tracker. Goodbye!",
            menu_options=[{"msg": "Import a CSV File", "fn": [self.data_management.use_csv, self.refresh_transactions, self.show_full_menu]}]
        )
        self.full_menu_options = [
                {"msg": "Import a CSV File", "fn": [self.data_management.use_csv, self.refresh_transactions]},
                {"msg": "View All Transactions", "fn": self.data_management.view},
                {"msg": "View Transactions by Date Range", "fn": lambda: self.data_management.view(dateRange=True)},
                {"msg": "Add a Transaction", "fn": [self.data_management.add, self.refresh_transactions]},
                {"msg": "Edit a Transaction", "fn": [self.data_management.edit, self.refresh_transactions]},
                {"msg": "Delete a Transaction", "fn": [self.data_management.delete, self.refresh_transactions]},
                {"msg": "Analyze Spending by Category", "fn": self.data_analysis.analyze_spending_by_category},
                {"msg": "Calculate Average Monthly Spending", "fn": self.data_analysis.calculate_average_monthly_spending},
                {"msg": "Show Top Spending Category", "fn": self.data_analysis.show_top_spending_category},
                {"msg": "Set Category Budget", "fn": [self.budget_management.set_category_budget, self.refresh_budget]},
                {"msg": "Check Budget Status", "fn": self.budget_management.check_budget_status},
                {"msg": "Show visualization menu", "fn": self.visualization.show_menu},
                {"msg": "Save Transactions to CSV", "fn": self.data_management.save}
            ]

    def run(self):
        self.menu_screen.run()
    
    def refresh_transactions(self):
        if self.data_management.transactions.empty:
            return
        self.data_analysis.data = self.data_management.transactions
        self.budget_management.data = self.data_management.transactions
        self.visualization.data = self.data_management.transactions
        self.visualization.spends_and_budget = self.budget_management.spends_and_budget
    
    def refresh_budget(self):
        if self.data_management.transactions.empty:
            return
        self.budget_management.data = self.data_management.transactions
        self.visualization.spends_and_budget = self.budget_management.spends_and_budget
    
    def show_full_menu(self):
        if self.data_management.transactions.empty:
            return
        self.menu_screen.menu_options = self.full_menu_options

def main():
    """Entry point of the application."""
    try:
        app = PersonalFinanceTracker()
        app.run()
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()