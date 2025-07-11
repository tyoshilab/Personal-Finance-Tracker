import pandas as pd
from validations import *
import glob

class DataManagement:
    def __init__(self):
        self.transactions = pd.DataFrame({
            'Date': pd.Series(dtype='datetime64[ns]'),
            'Category': pd.Series(dtype='str'),
            'Description': pd.Series(dtype='str'),
            'Amount': pd.Series(dtype='float'),
            'Type': pd.Series(dtype='str')
        })
        self.file_path = ""

    def use_csv(self):
        csv_files = glob.glob("*.csv")

        if not csv_files:
            print("No CSV files found in the current directory. Creating an empty DataFrame.")
            self.transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
            return
        
        for i, file in enumerate(csv_files, start=1):
            print(f"{i}. {file}")

        print("Please enter the number of the CSV file you want to import (or 'c' to cancel):")
        while True:
            user_input = input("> ").strip()
            if user_input.lower() == 'c':
                print("Inport cancelled.")
                return

            is_valid, _ = validate_number_in_range(user_input, 1, len(csv_files))
            if is_valid:
                break
            
        self.transactions = self.load_transactions(csv_files[int(user_input) - 1])

    def load_transactions(self, file_path) -> pd.DataFrame:
        try:
            transactions = pd.read_csv(file_path)
            transactions['Date'] = pd.to_datetime(transactions['Date'])
            print(f"Transactions loaded from {file_path} successfully!")
        except pd.errors.EmptyDataError:
            transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
        except Exception as e:
            print(f"An error occurred while loading transactions: {e}\nUsing an empty DataFrame.")
            transactions = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount', 'Type'])
        self.file_path = file_path
        return transactions

    def view(self, dateRange = False):
        if self.transactions.empty:
            print("No transactions found.")
        else:
            if dateRange:
                while True:
                    first_date = input("Enter the start date (YYYY-MM-DD): ")
                    is_valid, first_date = validate_date(first_date)
                    if is_valid:
                        break

                while True:
                    last_date = input("Enter the end date (YYYY-MM-DD): ")
                    is_valid, last_date = validate_date(last_date)
                    if is_valid:
                        break


                print(f"--- Transactions from {first_date.strftime('%Y-%m-%d')} to {last_date.strftime('%Y-%m-%d')} ---")

                mask = (self.transactions["Date"].dt.date >= first_date) & (
                            self.transactions["Date"].dt.date <= last_date)
                filtered_transactions = self.transactions[mask]
                ordered_transactions = filtered_transactions.sort_values('Date')
                print(ordered_transactions.to_string(index=False))
            else:
                print("--- All Transactions ---")

                printable_transactions = self.transactions.copy()
                printable_transactions["Date"] = printable_transactions["Date"].apply(lambda d: d.strftime("%Y-%m-%d") if pd.notnull(d) else "")
                print(printable_transactions.to_string(index=False))

    def add(self):
        print("--- Add Transactions ---")

        while True:
            print("Select the transaction type (1 or 2):")
            for i, t_type in enumerate(TRANSACTION_TYPES, start=1):
                print(f"{i}. {t_type}")
            trans_type = input()
            is_valid, trans_type = validate_transaction_type(trans_type)
            if is_valid:
                break

        while True:
            desc = input("Add the transaction description: ")
            is_valid = validate_text(desc)
            if is_valid:
                break

        while True:
            category = input("Add the category: ")
            is_valid = validate_text(category)
            if is_valid:
                break

        while True:
            amount = input("Add the amount: ")
            is_valid, amount = validate_money(amount)
            if is_valid:
                break

        while True:
            trans_date = input("Add the transaction date (YYYY-MM-DD): ")
            is_valid, trans_date = validate_date(trans_date)
            if is_valid:
                break

        transaction = {
            'Date': trans_date,
            'Category': category,
            'Description': desc,
            'Amount': amount,
            'Type': trans_type
        }

        new_transaction = pd.DataFrame([transaction])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

        print("Transaction added successfully.")


    def edit(self):
        print("--- Edit Transaction ---")

        if self.transactions.empty:
            print("No transactions to edit.")
            return

        for i, row in self.transactions.iterrows():
            print(f"{i}. {row['Date'].strftime('%Y-%m-%d')} | {row['Category']} | {row['Description']} | ${row['Amount']} | {row['Type']}")

        print("Enter the number of the transaction you want to edit (or 'c' to cancel):")

        while True:
            user_input = input("> ").strip()
            if user_input.lower() == 'c':
                print("Edit cancelled.")
                return

            is_valid, trans_id = validate_number_in_range(user_input, 0, len(self.transactions) - 1)
            if is_valid:
                break

        transaction = self.transactions.loc[trans_id].to_dict()

        print("Press Enter to keep current value.")

        while True:
            new_date = input(f"Date [{transaction['Date'].date()}]: ").strip()
            if not new_date:
                break
            is_valid, val = validate_date(new_date)
            if is_valid:
                transaction['Date'] = val.isoformat()
                break
            else:
                print("Invalid date. Please enter in YYYY-MM-DD format.")

        while True:
            new_cat = input(f"Category [{transaction['Category']}]: ").strip()
            if not new_cat:
                break
            is_valid = validate_text(new_cat)
            if is_valid:
                transaction['Category'] = new_cat
                break
            else:
                print("Category cannot be empty.")

        while True:
            new_desc = input(f"Description [{transaction['Description']}]: ").strip()
            if not new_desc:
                break
            is_valid = validate_text(new_desc)[0]
            if is_valid:
                transaction['Description'] = new_desc
                break
            else:
                print("Description cannot be empty.")

        while True:
            new_amount = input(f"Amount [{transaction['Amount']}]: ").strip()
            if not new_amount:
                break
            is_valid, val = validate_money(new_amount)
            if is_valid:
                transaction['Amount'] = val
                break
            else:
                print("Invalid amount. Must be a positive number.")

        while True:
            print("Transaction Types:")
            for idx, t_type in enumerate(TRANSACTION_TYPES, start=1):
                print(f"{idx}. {t_type}")
            new_type = input(f"Type [{transaction['Type']}]: ").strip()
            if not new_type:
                break
            is_valid, val = validate_transaction_type(new_type)
            if is_valid:
                transaction['Type'] = val
                break
            else:
                print("Invalid transaction type. Enter 1 or 2.")

        for key, value in transaction.items():
            self.transactions.at[trans_id, key] = value

        print("Transaction updated successfully.")

    def delete(self):
        print("--- Delete Transaction ---")

        if self.transactions.empty:
            print("No transactions to delete.")
            return

        for i, row in self.transactions.iterrows():
            print(f"{i}. {row['Date'].strftime('%Y-%m-%d')} | {row['Category']} | {row['Description']} | ${row['Amount']} | {row['Type']}")

        print("Enter the number of the transaction you want to delete (or 'c' to cancel):")

        while True:
            user_input = input("> ").strip()

            if user_input.lower() == 'c':
                print("Deletion cancelled.")
                return

            is_valid, trans_id = validate_number_in_range(user_input, 0, len(self.transactions) - 1)
            if is_valid:
                break

        self.transactions = self.transactions.drop(index=trans_id).reset_index(drop=True)

        print("Transaction deleted successfully.")

    def save(self):
        while True:
            input_file_path = input(f"Enter file path to save transactions(default is {self.file_path}): " or self.file_path).strip()
            if any(char in input_file_path for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']):
                print("Invalid file name. Please avoid using characters like /, \\, :, *, ?, \", <, >, |.")
                continue
            if not input_file_path.endswith('.csv'):
                input_file_path += '.csv'
            break
        try:
            self.transactions.to_csv(input_file_path, index=False)
        except PermissionError:
            print(f"Permission denied: Unable to save to {input_file_path}. Please close the file if it's open.")
            return
        except Exception as e:
            print(f"An error occurred while saving transactions: {e}")
            return
        print(f"Transactions saved to {input_file_path} successfully!")

