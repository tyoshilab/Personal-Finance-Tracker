class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_spending_by_category(self):
        print("TODO: Analyzing spending by category")
        spending_by_category = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
        print(spending_by_category)

    def calculate_average_monthly_spending(self):
        print("TODO: Calculating average monthly spending")
        data['Date'] = pd.to_datetime(data['Date'])
        monthly_spending = data[data['Type'] == 'Expense'].groupby(data['Date'].dt.month_name())['Amount'].mean()
        print(round(monthly_spending, 2))

    def show_top_spending_category(self):
        print("TODO: Showing top spending category")
        category_max = spending_by_category.idxmax()
        amount_max = spending_by_category.max()
        print(f'{category_max} with ${amount_max} total spending is the highest.')
    
    def visualize_monthly_spending_trend(self):
        print("TODO: Visualizing monthly spending trend")