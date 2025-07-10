import datetime

TRANSACTION_TYPES = ("Expense", "Income")

def validate_text(value):
    if not value.strip():
        return False
    return True

def validate_money(value):
    try:
        number = float(value)
        if number <= 0:
            print("Amount must be greater than zero.")
            return False, None
        number = round(number, 2)
        return True, number
    except ValueError:
        print("Please enter a valid amount.")
        return False, None

def validate_date(value):
    try:
        date_obj = datetime.datetime.strptime(value.strip(), "%Y-%m-%d").date()
        return True, date_obj
    except ValueError:
        print("Please enter a valid date.")
        return False, None

def validate_transaction_type(value):
    try:
        index = int(value)
        if 1 <= index <= len(TRANSACTION_TYPES):
            return True, TRANSACTION_TYPES[index - 1]
        else:
            print(f"Invalid option. Enter a number between 1 and {len(TRANSACTION_TYPES)}.")
            return False, None
    except ValueError:
        print("Please enter a valid number.")
        return False, None