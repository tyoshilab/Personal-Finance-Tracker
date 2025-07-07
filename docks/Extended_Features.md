**Final Project: Extended Features Income/Budget Management For +20 Bonus Points** 

In addition to tIf the user'```

If the user's spending is nearing the bud3. **Pie Chart for Income and Expense Distribution**:
   A pie chart shows the distribution of income and expenses, providing a clear view of how the user's money is allocated.limit:ending is nearing the budget limit: 

```
--- Budget Status ---
- Food: $480.00 / $500.00 (Warning: Close to budget!)
- Rent: $1200.00 / $1200.00
- Utilities: $180.00 / $200.00
- Transport: $140.00 / $150.00

Suggestions:
- Monitor food spending closely to avoid exceeding the budget.
- You are on track for other categories.
```

**4. Visualize Spending Trends**onalities of the **Personal Finance Tracker App**, this version includes **income and budget management** features. These enhancements will help users better manage their finances by tracking income, setting budgets, and providing alerts or suggestions when spending exceeds the budget. 

**Extended Features Description** 

1. **Income Management**: 

Users can enter their income details, which will be used to calculate total income over a specified period. 

This allows users to compare income to expenses and understand their financial balance. 

2. **Budget Setting and Alerts**: 

Users can set a budget for specific categories (e.g., Food, Rent, Utilities) or an overall monthly budget. 

The app will compare spending against the budget: 

- If spending exceeds the budget, it will alert the user with a message. 
- If spending is close to the budget (e.g., within 10%), it will warn the user. 
- It will suggest adjustments like reducing specific category spending to stay within budget. 

3. **Suggestions for Better Budgeting**: 

Based on the analysis of spending patterns, the app will provide suggestions, such as: 

- Reducing spending on non-essential categories.
- Saving more in months with lower spending. 
- Adjusting the budget based on average spending trends. 

**Sample Output for Income/Budget Management** 

Below are sample outputs demonstrating how the new income and budget management features will behave within the **Personal Finance Tracker App**. These outputs are based on interactions using the provided `sampledata.csv`. 

**Initial Menu Display with Extended Features** 

When users start the app, the main menu now includes options for income and budget management: 

```
=== Personal Finance Tracker ===
0. Import a CSV File
1. View All Transactions
2. View Transactions by Date Range
3. Add a Transaction
4. Edit a Transaction
5. Delete a Transaction
6. Analyze Spending by Category
7. Calculate Average Monthly Spending
8. Show Top Spending Category
9. Set Monthly Income
10. Set Category Budget
11. Check Budget Status
12. Visualize Spending Trends
13. Save Transactions to CSV
14. Exit

Choose an option (1-14):
```

**1. Set Monthly Income** 

If the user chooses this option, they can set their monthly income:

```
Enter your total monthly income: 3000.00
Your monthly income is set to: $3000.00
```

**2. Set Category Budget** 

If the user chooses this option, they can set budgets for specific categories: 

```
Enter your budget for Food: 500.00
Enter your budget for Rent: 1200.00
Enter your budget for Utilities: 200.00
Enter your budget for Transport: 150.00

Your budgets have been set:
- Food: $500.00
- Rent: $1200.00
- Utilities: $200.00
- Transport: $150.00
```

**3. Check Budget Status** 

This option compares actual spending against the set budget and displays alerts or suggestions: 

```
--- Budget Status ---
- Food: $200.75 / $500.00
- Rent: $2400.00 / $1200.00 (Alert: Exceeded budget!)
- Utilities: $100.00 / $200.00
- Transport: $27.75 / $150.00

Suggestions:
- Consider reducing rent spending or adjusting the budget.
- You are within budget for other categories. Keep up the good work!
```

Final Project: Extended Features Income/Budget Management For 20 Bonus Points 3   
If the user’s spending is nearing the budget limit: 

\--- Budget Status \--- 

\- Food: $480.00 / $500.00 (Warning: Close to budget\!) \- Rent: $1200.00 / $1200.00 

\- Utilities: $180.00 / $200.00 

\- Transport: $140.00 / $150.00 

Suggestions: 

\- Monitor food spending closely to avoid exceeding the budge t. 

\- You are on track for other categories. 

**4\. Visualize Spending Trends** 

This option visualizes income, spending, and budget trends using charts:

1. **Line Chart for Monthly Income vs. Spending**: 
   A line chart opens showing monthly income compared to total spending. 

   ```
   [Line Chart Opens]
   - X-axis: Months
   - Y-axis: Amount
   - Line 1: Total Income
   - Line 2: Total Spending
   ```

2. **Bar Chart for Category Spending vs. Budget**: 
   A bar chart displays category-wise spending against the set budget. 

   ```
   [Bar Chart Opens]
   - X-axis: Categories (e.g., Food, Rent, Utilities)
   - Y-axis: Amount
   - Bars: Actual Spending vs. Budget
   ```

3. **Pie Chart for Income and Expense Distribution**:

Final Project: Extended Features Income/Budget Management For 20 Bonus Points 4   
A pie chart shows the distribution of income and expenses, providing a clear view of how the user’s money is allocated. 
   ```
   [Pie Chart Opens]
   - Slices: Income, Food, Rent, Utilities, Transport, etc.
   ```

**Example Output Using sampledata.csv** 

**Viewing All Transactions** 

If the user selects this option, it displays the content of the `sampledata.csv` file: 

```
--- All Transactions ---
 Date         Category    Description        Amount    Type
0  2024-10-01  Food        Grocery            50.75    Expense
1  2024-10-02  Rent        Monthly Rent     1200.00    Expense
2  2024-10-02  Utilities   Electricity Bill   60.00    Expense
3  2024-10-03  Food        Dinner             30.00    Expense
4  2024-10-04  Transport   Bus Ticket          2.75    Expense
5  2024-10-05  Food        Breakfast          15.00    Expense
6  2024-10-06  Income      Salary           2000.00    Income
7  2024-10-10  Income      Freelance Work    500.00    Income
8  2024-10-12  Utilities   Water Bill         40.00    Expense
9  2024-10-15  Food        Lunch              25.00    Expense
10 2024-10-18  Transport   Taxi               25.00    Expense
11 2024-10-20  Income      Investment Return 200.00    Income
12 2024-10-25  Food        Groceries          80.00    Expense
13 2024-10-28  Rent        Monthly Rent     1200.00    Expense
```

**Saving Transactions to CSV** 

If the user selects this option, they can save the updated transactions list to a CSV file: 

```
Enter file name to save (e.g., 'transactions.csv'): updated_transactions.csv
Transactions saved to updated_transactions.csv successfully!
```

**Final Summary** 

- **Income and Budget Management**: Helps users track income, set budgets, and manage finances effectively. 
- **Alerts and Suggestions**: Provides real-time feedback on spending patterns. 
- **Visualizations**: Offers a clear graphical representation of financial trends, making it easier for users to understand their financial health. 