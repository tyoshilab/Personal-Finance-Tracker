import matplotlib.pyplot as plt
from menu_screen import MenuScreen
import pandas as pd

class DataVisualization:
    def __init__(self, data, spends_and_budget):
        self.data = data
        self.spends_and_budget = spends_and_budget
        self.menu_screen = MenuScreen(
            top_message="=== Visualization Menu ===",
            exit_message="Returning to main menu...",
            menu_options = [
                {"msg": "monthly spending trend", "fn": self.monthly_spending_trend},
                {"msg": "spending by category", "fn": self.spending_by_category},
                {"msg": "percentage of spending by category", "fn": self.percentage_categories},
                {"msg": "monthly income vs spending", "fn": self.monthly_income_vs_spending},
                {"msg": "visualize category spending vs budget", "fn": self.category_spending_vs_budget},
                {"msg": "visualize income and expenses", "fn": self.income_and_expenses},
            ]
        )
        
    def show_menu(self):
        self.menu_screen.run()
        self.menu_screen.is_running = True

    def monthly_spending_trend(self):
        monthly_data = self.data[['Date', 'Amount']].groupby(self.data['Date'].dt.to_period('M')).sum('Amount')
        plt.plot(monthly_data.index.astype(str), monthly_data['Amount'], marker='o')
        plt.title('Monthly Spending Trend')
        plt.xlabel('Month')
        plt.ylabel('Total Spending')
        print("Visualizing monthly spending trend...")
        plt.show()

    def spending_by_category(self):
        category_data = self.data.groupby('Category')['Amount'].sum().sort_values(ascending=False)
        plt.bar(category_data.index, category_data.values)
        plt.title('Spending by Category')
        plt.xlabel('Category')
        plt.ylabel('Total Spending')
        print("Visualizing spending by category...")
        plt.show()
    
    def percentage_categories(self):
        category_data = self.data.groupby('Category')['Amount'].sum()
        plt.pie(category_data, labels=category_data.index, autopct='%1.1f%%', startangle=140)
        plt.title('Spending Distribution by Category')
        print("Visualizing spending distribution by category...")
        plt.show()

    def monthly_income_vs_spending(self):
        monthly_data = self.data.copy()
        monthly_data['Month'] = monthly_data['Date'].dt.to_period('M')
        
        monthly_summary = monthly_data.groupby(['Month', 'Type'])['Amount'].sum().unstack(fill_value=0)
        
        # Extract income and expense data, handle missing columns
        income_data = monthly_summary.get('Income', pd.Series(0, index=monthly_summary.index))
        expense_data = monthly_summary.get('Expense', pd.Series(0, index=monthly_summary.index))
        months = monthly_summary.index.astype(str)
        
        plt.plot(months, income_data, marker='o', label='Income', color='blue', linewidth=2)
        plt.plot(months, expense_data, marker='o', label='Expense', color='orange', linewidth=2)
        plt.title('Monthly Income vs Spending')
        plt.ylabel('Amount')
        plt.legend()
        plt.grid(True, alpha=0.3)
        print("Visualizing monthly income vs spending...")
        plt.show()

    def category_spending_vs_budget(self):
        if self.spends_and_budget is None:
            print("You need to check your Budget Status")
            return
        print("Visualizing spending distribution")
        print(self.spends_and_budget)
        self.spends_and_budget.set_index('Category')['Budget'].plot(kind='bar')
        self.spends_and_budget.set_index('Category')['Amount'].plot(kind='bar', color='red', alpha=0.5)
        plt.show()

    def income_and_expenses(self):
        df = self.data.copy()
        df.loc[df['Type']=='Income','Category'] = 'Income'

        plt.pie(df.groupby('Category')['Amount'].sum(), labels=df.groupby('Category')['Amount'].sum().index, autopct='%1.1f%%')
        plt.title('Income and Expenses Distribution')
        print("Visualizing income and expenses distribution...")
        plt.show()

