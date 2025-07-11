import os
import sys
from data_management import DataManagement
from data_analysis import DataAnalysis
from visualization import DataVisualization
from budget_management import BudgetManagement

class PersonalFinanceTracker:
    def __init__(self):
        self.data_management = DataManagement()
        self.data_analysis = DataAnalysis(self.data_management.transactions)
        self.budget_management = BudgetManagement(self.data_management.transactions)
        self.visualization = DataVisualization(self.data_management.transactions)
        self.is_running = True
        self.valid_message = ""
        self.menu_options = [
            #TODO import a csv from file explorer
            {"msg": "Import a CSV File", "fn": [self.data_management.use_csv, self.refresh_transactions]},
            {"msg": "View All Transactions", "fn": self.data_management.view},
            {"msg": "View Transactions by Date Range", "fn": lambda: self.data_management.view(dateRange=True)},
            {"msg": "Add a Transaction", "fn": [self.data_management.add, self.refresh_transactions]},
            {"msg": "Edit a Transaction", "fn": [self.data_management.edit, self.refresh_transactions]},
            {"msg": "Delete a Transaction", "fn": [self.data_management.delete, self.refresh_transactions]},
            {"msg": "Analyze Spending by Category", "fn": self.data_analysis.analyze_spending_by_category},
            {"msg": "Calculate Average Monthly Spending", "fn": self.data_analysis.calculate_average_monthly_spending},
            {"msg": "Show Top Spending Category", "fn": self.data_analysis.show_top_spending_category},
            {"msg": "Set Category Budget", "fn": self.budget_management.set_category_budget},
            {"msg": "Check Budget Status", "fn": self.budget_management.check_budget_status},
            {"msg": "Show visualization menu", "fn": self.visualization.show_menu},
            {"msg": "Save Transactions to CSV", "fn": self.data_management.save},
            {"msg": "Exit", "fn": self._exit_program}
        ]

    def run(self):
        """Main application loop."""
        while self.is_running:
            self._show_main_menu()

            choice = self._get_user_choice()
            if choice is None:
                continue
            
            os.system('cls' if os.name == 'nt' else 'clear')
            self._execute_menu_option(choice)
            
            if self.is_running:  # Only wait if not exiting
                input("\nPress Enter to continue...")
    
    def _show_main_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display validation messages to the user
        if self.valid_message:
            print(f"{self.valid_message}\n")
            self.valid_message = ""
        
        print("=== Personal Finance Tracker ===")
        print()
        for index, option in enumerate(self.menu_options, start=1):
            print(f"{index}. {option['msg']}")

    def _get_user_choice(self):
        """Get and validate user menu choice."""
        menu_count = len(self.menu_options)
        
        try:
            choice = int(input(f"Choose an option (1-{menu_count}): "))
            if not (1 <= choice <= menu_count):
                self.valid_message = f"Invalid selection. Please choose a number between 1 and {menu_count}."
                return None
            return choice
        except ValueError:
            self.valid_message = f"Invalid input. Please enter a number between 1 and {menu_count}."
            return None
        except KeyboardInterrupt:
            self.valid_message = "\nOperation cancelled by user."
            return None
        except Exception as e:
            self.valid_message = f"An unexpected error occurred: {e}"
            return None
    
    def _execute_menu_option(self, choice):
        """Execute the selected menu option."""
        try:
            selected_option = self.menu_options[choice - 1]
            print(f"You selected: {choice}. {selected_option['msg']}\n")
            
            # Execute the selected function
            fns = selected_option["fn"]

            if isinstance(fns, list):
                for fn in fns:
                    fn()
            else:
                fns()
                
        except Exception as e:
            self.valid_message = f"Error executing menu option: {e}"
        
    def _exit_program(self):
        """Exit the application gracefully."""
        self.is_running = False
        print("Exiting the Personal Finance Tracker. Goodbye!")

    def refresh_transactions(self):
        self.data_analysis.data = self.data_management.transactions
        self.visualization.data = self.data_management.transactions
        self.budget_management.data = self.data_management.transactions

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