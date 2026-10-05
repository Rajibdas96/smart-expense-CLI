from datetime import datetime
import json
import os



transactions = []

def generate_transaction_id():
    if os.path.exists("user_storage.json")and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                return 1
    else:
        return 1

def clean_and_reindex(transactions_list):
    for index, transaction in enumerate(transactions_list):
        transaction['id'] = index + 1
    return transactions_list


def main_menu():
    while True:
        print("-----------------------------")
        print("SMART EXPENSE TRACKER")
        print("-----------------------------")
        print("1.ADD EXPENSE")
        print("2.VIEW EXPENSE")
        print("3.TOTAL EXPENSE")
        print("4.SEARCH/FILTER")
        print("5.DELETE EXPENSE")
        print("6.EDIT EXPENSE")
        print("7.EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            search_filter()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            edit_expense()
        elif choice == "7":
            print("-----------------------------")
            print("Exiting the program....")
            print("Thank you for using the Smart Expense Tracker. Goodbye!")
            print("-----------------------------")
            break
        else:
            print("Invalid Number...Please Try Again.")


def add_expense():
    print("-----------------------------")
    print("ADD EXPENSE")
    print("-----------------------------")
    while True:
        try:
            expense_amount = float(input("Enter the expense amount: "))
            if expense_amount <=0:
                print ("Invalid Number")
                continue
            break
        except ValueError:
            print("you must put decimal number.")
    
    while True:
        print("Select the expense category")
        print("1. FOOD")
        print("2. TRANSPORTATION")
        print("3. ENTERTAINMENT")
        print("4. SHOPPING")
        print("5. BILLS")
        print("6. HEALTHCARE")
        print("7. OTHER")

        expense_category = input("Enter your choice: ")
        if expense_category == "1":
            expense_category = "FOOD"
            break
        elif expense_category == "2":
            expense_category = "TRANSPORTATION"
            break
        elif expense_category == "3":
            expense_category = "ENTERTAINMENT"
            break
        elif expense_category == "4":
            expense_category = "SHOPPING"
            break
        elif expense_category == "5":
            expense_category = "BILLS"
            break
        elif expense_category == "6":
            expense_category = "HEALTHCARE"
            break
        elif expense_category == "7":
            expense_category = "OTHER"
            break
        else:
            print("Invalid choice. Please try again and choose a valid option.")
        
    expense_description = input("Enter the expense description: ")
    now = datetime.now()
    if os.path.exists("user_storage.json") and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                transactions = []
    else:
        transactions = []
    transaction = {
        "id": generate_transaction_id(transactions),
        "amount": expense_amount,
        "category": expense_category,
        "description": expense_description,
        "Date Time" : now.strftime("%Y-%m-%d %H:%M")
    }
    transactions.append(transaction)
    with open("user_storage.json", "w") as f:
        json.dump(transactions, f, indent=4)
        transactions = clean_and_reindex(transactions)
        with open("user_storage.json", "w") as f:
            json.dump(transactions, f, indent=4)
    print("EXPENSE DETAILED")
    print(f"Amount: {expense_amount}\nCategory: {expense_category}\nDescription: {expense_description}\nDate Time: {transaction['Date Time']}")
    print("-----------------------------")
    print("Expense Added Successfully👍")
    print("-----------------------------")


def generate_transaction_id(transactions_list):
    if not transactions_list:
        return 1
    highest_id = max(transaction["id"] for transaction in transactions_list)
    return highest_id + 1

def view_expense():
    print("-----------------------------")
    print("VIEW EXPENSE")
    print("-----------------------------")
    if os.path.exists("user_storage.json") and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                transactions = []
    else:
        transactions = []
    if len(transactions) == 0:
        print("No expense found")
    else:
        for i, transaction in enumerate(transactions):
            print(f"Transaction: {transaction['id']}")
            print(f"Amount: {transaction['amount']}")
            print(f"Category: {transaction['category']}")
            print(f"Description: {transaction['description']}")
            print(f"Date time: {transaction['Date Time']}")
    print("-----------------------------")

def total_expense():
    print("-----------------------------")
    print("TOTAL EXPENSE")
    print("-----------------------------")
    if os.path.exists("user_storage.json") and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                transactions = []
    else:
        transactions = []

    if not transactions:
        print("No expense found")
    else:
        Food = sum(t['amount'] for t in transactions if t['category'] == 'FOOD')
        print(f"Total Expense for FOOD: {Food} RS.")
        Transportation = sum(t['amount'] for t in transactions if t['category'] == 'TRANSPORTATION')
        print(f"Total Expense for TRANSPORTATION: {Transportation} RS.")
        Entertainment = sum(t['amount'] for t in transactions if t['category'] == 'ENTERTAINMENT')
        print(f"Total Expense for ENTERTAINMENT: {Entertainment} RS.")
        Shopping = sum(t['amount'] for t in transactions if t['category'] == 'SHOPPING')
        print(f"Total Expense for SHOPPING: {Shopping} RS.")
        Bills = sum(t['amount'] for t in transactions if t['category'] == 'BILLS')
        print(f"Total Expense for BILLS: {Bills} RS.")
        Healthcare = sum(t['amount'] for t in transactions if t['category'] == 'HEALTHCARE')
        print(f"Total Expense for HEALTHCARE: {Healthcare} RS.")
        Other = sum(t['amount'] for t in transactions if t['category'] == 'OTHER')
        print(f"Total Expense for OTHER: {Other} RS.")
        total = sum(t['amount'] for t in transactions)
        print(f"Total Expense: {total} RS.")
    print("-----------------------------")

def search_filter():
    print("-----------------------------")
    print("SEARCH/FILTER")
    print("-----------------------------")
    if os.path.exists("user_storage.json") and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                transactions = []
    valid_categories = ["FOOD", "TRANSPORTATION", "ENTERTAINMENT", "SHOPPING", "BILLS", "HEALTHCARE", "OTHER"]
    filter_by = input("Filter by: ").strip().upper()
    if filter_by not in valid_categories:
        print("Invalid filter. Please try again.")
        print("-----------------------------")
        return
    filtered_transactions = [t for t in transactions if t['category'] == filter_by]

    print("-----------------------------")
    print("FILTERED TRANSACTIONS")
    print("-----------------------------")
    for i, transaction in enumerate(filtered_transactions):
        print(f"Transaction: {transaction['id']}")
        print(f"Amount: {transaction['amount']}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Date time: {transaction['Date Time']}")
    print("-----------------------------")

def delete_expense():
    print("-----------------------------")
    print("DELETE EXPENSE")
    print("-----------------------------")
    if os.path.exists("user_storage.json") and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                transactions = []
    else:
        transactions = []
    transaction_id = input("Enter the transaction ID to delete: ")
    for transaction in transactions:
        if transaction['id'] == int(transaction_id):
            print(f"Are you sure you want to delete this transaction {transaction['id']}? (y/n)")
            if input().lower() == 'y':
                transactions.remove(transaction)
                with open("user_storage.json", "w") as f:
                    json.dump(transactions, f, indent=4)
                    transactions = clean_and_reindex(transactions)
                    with open("user_storage.json", "w") as f:
                        json.dump(transactions, f, indent=4)
                print("Transaction deleted successfully.")
                print("-----------------------------")
            return
    update_transactions = [t for t in transactions if t['id'] != int(transaction_id)]
    with open("user_storage.json", "w") as f:
        json.dump(update_transactions, f, indent=4)
    print("No transaction found with the given ID.")
    print("-----------------------------")
    
def edit_expense():
    print("-----------------------------")
    print("EDIT EXPENSE")
    print("-----------------------------")
    transaction_id = input("Enter the transaction ID to edit: ")
    if os.path.exists("user_storage.json") and os.path.getsize("user_storage.json") > 0:
        with open("user_storage.json", "r") as f:
            try:
                transactions = json.load(f)
            except json.JSONDecodeError:
                transactions = []
    try:
        transaction_id = int(transaction_id)
    except ValueError:
        print("Invalid transaction ID. Please enter a valid number.")
        print("-----------------------------")
        return
    transaction_found = False
    for transaction in transactions:
        if transaction['id'] == int(transaction_id):
            transaction_found = True
            print("Enter new details (Leave blank to keep current value)")
            print(f"Current Amount: {transaction['amount']}")
            new_amount = input(f"New Amount: ")
            print(f"Current Category: {transaction['category']}")
            new_category = input(f"New Category: ")
            print(f"Current Description: {transaction['description']}")
            new_description = input(f"New Description: ")
            if new_amount:
                transaction['amount'] = float(new_amount)
            if new_category:
                transaction['category'] = new_category
            if new_description:
                transaction['description'] = new_description
            break
    if not transaction_found:
        print("No transaction found with the given ID.")
        print("-----------------------------")
    with open("user_storage.json", "w") as f:
        json.dump(transactions, f, indent=4)

    print("Transaction updated successfully.")
    print("-----------------------------")

if __name__ == "__main__":
    main_menu()