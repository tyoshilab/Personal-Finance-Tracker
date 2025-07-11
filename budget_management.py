# Manages income, budget setting, and alerts.
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

class BudgetManagement:
    def __init__(self, data):
        self._data = data
        self.categories = None
        self.budget_category_df = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self.categories = self.data['Category'].unique()
        
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
        return self.budget_category_df

    def check_budget_status(self):
        if self.budget_category_df is None:
            print("You need to set your budget")
            return

        print("Budget Status Checking")
        self.data['Date'] = pd.to_datetime(self.data['Date'])
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
        return self.spends_and_budget

# data = pd.read_csv('sampledata.csv')
# budget_category = {'Category': ['Food', 'Rent', 'Utilities', 'Transport'], 'Budget': [100, 1200, 300, 100]}
# budget_category_df = pd.DataFrame(budget_category)
#
# data['Date'] = pd.to_datetime(data['Date'])
# current_month = datetime.now().strftime("%B")
# current_year =  int(datetime.now().strftime("%Y"))
# print(current_month)
# print(current_year)
#
# spending_by_category_df = data[data['Type'] == 'Expense'].groupby([data['Date'].dt.year.rename('Year'),
#                                                                 data['Date'].dt.month_name().rename('Month'),
#                                                                 'Category'])['Amount'].sum()
# print(spending_by_category_df)
#
# spending_by_category_current_month = spending_by_category_df.reset_index()[
#     (spending_by_category_df['Month'] == current_month) &
#     (spending_by_category_df['Year'] == current_year)]
#
# print(spending_by_category_current_month)
# print(budget_category_df)
#
# spends_and_budget = pd.merge(budget_category_df, spending_by_category_current_month, on='Category')
# print(spends_and_budget)
#
# data = pd.read_csv('sampledata.csv')
#
# # Ensure 'Date' column is datetime type
# data['Date'] = pd.to_datetime(data['Date'])
#
# # Get current year and month
# current_month = datetime.now().strftime("%B")     # e.g., "July"
# current_year = int(datetime.now().strftime("%Y")) # e.g., 2025
#
# # Group expenses by Year, Month, and Category
# spending_by_category = data[data['Type'] == 'Expense'].groupby(
#     [data['Date'].dt.year.rename('Year'),
#      data['Date'].dt.month_name().rename('Month'),
#      'Category'])['Amount'].sum()
#
# # Reset index safely
# spending_by_category_df = spending_by_category.reset_index()
#
# # Filter for current year and month
# spending_current_month_df = spending_by_category_df[
#     (spending_by_category_df['Year'] == current_year) &
#     (spending_by_category_df['Month'] == current_month)
# ]
#
# # Display result
# print(spending_current_month_df)
# spends_and_budget = pd.merge(budget_category_df, spending_current_month_df, on='Category')
# print(spends_and_budget)
# spends_and_budget.set_index('Category')['Budget'].plot(kind='bar')
# spends_and_budget.set_index('Category')['Amount'].plot(kind='bar', color = 'red', alpha = 0.5)
# plt.show()