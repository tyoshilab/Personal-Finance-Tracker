# Manages income, budget setting, and alerts.
import pandas as pd
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

        spending_by_category = self.data[self.data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
        spends_and_budget = pd.merge(self.budget_category_df, spending_by_category, on='Category')
        categories_exceeded = []
        categories_close = []
        for index, row in spends_and_budget.iterrows():
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