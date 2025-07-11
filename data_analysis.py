from datetime import datetime
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
        monthly_spending = self.data[self.data['Type'] == 'Expense'].groupby([self.data['Date'].dt.year.rename('Year'),
                                                           self.data['Date'].dt.month_name().rename('Month')])['Amount'].mean()
        print(round(monthly_spending, 2))
        current_month = datetime.now().strftime("%B")
        current_year = int(datetime.now().strftime("%Y"))
        monthly_spending_df = monthly_spending.reset_index()
        current_avg = monthly_spending_df[(monthly_spending_df['Month'] == current_month) &
                                       (monthly_spending_df['Year'] == current_year)]['Amount'].mean()
        print(f'Current average spending: ${current_avg}  at {current_month},{current_year}.')

    def show_top_spending_category(self):
        print("Showing top spending category")
        category_max = self.spending_by_category.idxmax()
        amount_max = self.spending_by_category.max()
        print(f'{category_max} with ${amount_max} total spending is the highest.')

# current_month = datetime.now().strftime("%B")
# current_year = int(datetime.now().strftime("%Y"))
# print(current_month, current_year)