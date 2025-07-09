import pandas as pd
class DataManagement:
    def __init__(self, file_path='transactions.csv'):
        self.file_path = file_path
        self.transactions = self.load_transactions()

    def load_transactions(self) -> pd.DataFrame:
        try:
            transactions = pd.read_csv(self.file_path)
            transactions['Date'] = pd.to_datetime(transactions['Date'])
        except FileNotFoundError:
            transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
        except pd.errors.EmptyDataError:
            transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
        except Exception as e:
            print(f"An error occurred while loading transactions: {e}")
            transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
        
        return transactions
    
    def view(self, dateRange = False):
        if self.transactions.empty:
            print("No transactions found.")
        else:
            if dateRange:
                # dateRange logic would go here
                print("--- Transactions from 2024-10-02 to 2024-10-03 ---")
            else:
                print("--- All Transactions ---")

    def add(self):
        print("TODO: Adding a new transaction")

    def edit(self):
        print("TODO: Editing an existing transaction")

    def delete(self):
        print("TODO: Deleting a transaction")

    def save(self):
        print("TODO: Saving transactions to CSV")
