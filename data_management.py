import pandas as pd

class DataManagement:
    def __init__(self):
        self.transactions = pd.DataFrame(columns=['date', 'category', 'description', 'amount', 'type'])

    def use_csv(self):
        file_path = "sampledata.csv"
        self.transactions = self.load_transactions(file_path)

    def load_transactions(self, file_path) -> pd.DataFrame:
        try:
            transactions = pd.read_csv(file_path)
        except FileNotFoundError:
            transactions = pd.DataFrame(columns=['date', 'category', 'description', 'amount', 'type'])
        except pd.errors.EmptyDataError:
            transactions = pd.DataFrame(columns=['date', 'category', 'description', 'amount', 'type'])
        except Exception as e:
            print(f"An error occurred while loading transactions: {e}")
            transactions = pd.DataFrame(columns=['date', 'category', 'description', 'amount', 'type'])

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
                print(self.transactions)

    def add(self):
        print("TODO: Adding a new transaction")

    def edit(self):
        print("TODO: Editing an existing transaction")

    def delete(self):
        print("TODO: Deleting a transaction")

    def save(self):
        print("TODO: Saving transactions to CSV")
