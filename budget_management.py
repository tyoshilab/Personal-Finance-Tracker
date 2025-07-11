# Manages income, budget setting, and alerts.
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

class BudgetManagement:
    def __init__(self, data):
        self._data = data
        self.categories = None
        self.budget_category_df = None
        self.spends_and_budget = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self.categories = self.data['Category'].unique()
        self.calc_spends_and_budget()
        
    def set_category_budget(self):
        print("Set your budget")
        budget_category = {'Category': [], 'Budget': []}
        for i in range(len(self.categories)):
            if self.categories[i] != 'Income':
                x = float(input(f"Enter your budget for {self.categories[i]}: "))
                budget_category['Category'].append(self.categories[i])
                budget_category['Budget'].append(x)
        print("Your budget is now set to:")
        self.budget_category_df = pd.DataFrame(budget_category)
        for index, row in self.budget_category_df.iterrows():
            print(f"- {row['Category']}: ${row['Budget']}")
    
    def calc_spends_and_budget(self):
        if self.budget_category_df is None:
            return
        current_month = datetime.now().strftime("%B")
        current_year = int(datetime.now().strftime("%Y"))
        spending_by_category = self.data[self.data['Type'] == 'Expense'].groupby([self.data['Date'].dt.year.rename('Year'),
                                                                        self.data['Date'].dt.month_name().rename('Month'),
                                                                        'Category'])['Amount'].sum()
        spending_by_category_df = spending_by_category.reset_index()
        spending_current_month_df = spending_by_category_df[
            (spending_by_category_df['Year'] == current_year) &
            (spending_by_category_df['Month'] == current_month)]
        self.spends_and_budget = pd.merge(self.budget_category_df, spending_current_month_df, on='Category')

    def check_budget_status(self):
        if self.budget_category_df is None:
            print("You need to set your budget")
            return

        print("Budget Status Checking")

        categories_exceeded = []
        categories_close = []
        for index, row in self.spends_and_budget.iterrows():
            if row['Budget'] < row['Amount']:
                print(f"- {row['Category']}: ${row['Amount']} / ${row['Budget']} (Alert: Exceeded budget!)")
                categories_exceeded.append(row['Category'])
            elif 1 > row['Amount'] / row['Budget'] > 0.95:
                print(f"- {row['Category']}: ${row['Amount']} / ${row['Budget']} (Warning: Close to budget)")
                categories_close.append(row['Category'])
            else:
                print(f"- {row['Category']}: ${row['Amount']} / ${row['Budget']}")
        print('Suggestions:')
        if len(categories_exceeded) > 0:
            print('- Consider reducing your spends or adjust the budget on the following:')
            for category in categories_exceeded:
                print(f"  * {category}")
        if len(categories_close) > 0:
            print('- Monitor spends closely to avoid exceeding the budget on the following:')
            for category in categories_close:
                print(f"  * {category}")
        if len(categories_close) + len(categories_exceeded) < len(self.categories):
            print('- You are on track for other categories.')