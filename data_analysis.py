class DataAnalysis:
    def __init__(self, data):
        self._data = data
        self.spending_by_category = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self.spending_by_category = self._data[self.data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    
    def analyze_spending_by_category(self):
        print("Analyzing spending by category")
        print(self.spending_by_category)

    def calculate_average_monthly_spending(self):
        print("Calculating average monthly spending")
        monthly_spending = self.data[self.data['Type'] == 'Expense'].groupby(self.data['Date'].dt.month_name())['Amount'].mean()
        print(round(monthly_spending, 2))

    def show_top_spending_category(self):
        print("Showing top spending category")
        category_max = self.spending_by_category.idxmax()
        amount_max = self.spending_by_category.max()
        print(f'{category_max} with ${amount_max} total spending is the highest.')