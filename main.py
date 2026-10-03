from datetime import datetime
import json



transactions = []


def main_menu():
    while True:
        print("SMART EXPENSE TRACKER")
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
            print("Exiting the program....")
            break
        else:
            print("Invalid Number...Please Try Again.")


def add_expense():
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
    transaction = {
        "id": generate_transaction_id(),
        "amount": expense_amount,
        "category": expense_category,
        "description": expense_description,
        "Date Time" : now.strftime("%Y-%m-%d %H:%M"),
    }
    with open("user_storage.json", "w") as f:
        json.dump(transactions, f, indent=4)
    transactions.append(transaction)
    print("EXPENSE DETAILED")
    print(f"Amount: {expense_amount}\nCategory: {expense_category}\nDescription: {expense_description}\nDate Time: {transaction['Date Time']}")
    print("-----------------------------")
    print("Expense Added Successfully👍")
    print("-----------------------------")


def generate_transaction_id():
    if not transactions:
        return 1
    highest_id = max(transaction["id"] for transaction in transactions)
    return highest_id + 1

def view_expense():
    print("VIEW EXPENSE")
    print("-----------------------------")
    if len(transactions) == 0:
        print("No expense found")
    else:
        for i, transaction in enumerate(transactions):
            print(f"Transaction: {i+1}")
            print(f"Amount: {transaction['amount']}")
            print(f"Category: {transaction['category']}")
            print(f"Description: {transaction['description']}")
            print(f"Date time: {transaction['Date Time']}")
    print("-----------------------------")

def total_expense():
    print("TOTAL EXPENSE")
    print ("-----------------------------")
    total = sum(t['amount'] for t in transactions)
    print(f"Total Expense: {total}")
    print("-----------------------------")
def search_filter():
    print("SEARCH/FILTER")
    valid_categories = ["FOOD", "TRANSPORTATION", "ENTERTAINMENT", "SHOPPING", "BILLS", "HEALTHCARE", "OTHER"]
    filter_by = input("Filter by: ").strip().upper()
    if filter_by not in valid_categories:
        print("Invalid filter. Please try again.")
        print("-----------------------------")
        return
    filtered_transactions = [t for t in transactions if t['category'] == filter_by]

    print("FILTERED TRANSACTIONS")
    print("-----------------------------")
    for i, transaction in enumerate(filtered_transactions):
        print(f"Transaction: {i+1}")
        print(f"Amount: {transaction['amount']}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Date time: {transaction['Date Time']}")
    print("-----------------------------")

def delete_expense():
    print("DELETE EXPENSE")
    print("-----------------------------")
    transaction_id = input("Enter the transaction ID to delete: ")
    for transaction in transactions:
        if transaction['id'] == int(transaction_id):
            print("Are you sure you want to delete this transaction? (y/n)")
            if input().lower() == 'y':
                transactions.remove(transaction)
                with open("user_storage.json", "w") as f:
                    json.dump(transactions, f, indent=4)
                print("Transaction deleted successfully.")
                print("-----------------------------")
            return
    print("No transaction found with the given ID.")
    print("-----------------------------")
    
def edit_expense():
    print("EDIT EXPENSE")
    print("-----------------------------")
    transaction_id = input("Enter the transaction ID to edit: ")
    for transaction in transactions:
        if transaction['id'] == int(transaction_id):
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
            print("Transaction updated successfully.")
            print("-----------------------------")
            return
        print("No transaction found with the given ID.")
        print("-----------------------------")
        

if __name__ == "__main__":
    main_menu()