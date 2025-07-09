import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, data):
        self.data = data

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
        print("ex_TODO: Visualizing monthly income vs spending")

    def category_spending_vs_budget(self):
        print("ex_TODO: Visualizing spending distribution")

    def income_and_expenses(self):
        print("ex_TODO: Visualizing income and expenses")