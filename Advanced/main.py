import getpass
from auth import register, login
from expense_manager import log_transaction, view_transactions, visualize_transactions
from database import db

def main():
    db()
    
    print("Welcome to Personal Finance Manager")
    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            register(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            if login(username, password):
                user_dashboard(username)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def user_dashboard(username):
    print(f"\nWelcome, {username}!")
    while True:
        print("\n1. Log Transaction")
        print("\n2. View Transactions")
        print("\n3. Visualize Transactions")
        print("\n4. Logout")
        
        choice = input("Enter choice: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            trans_type = input("Enter type (income/expense): ")
            log_transaction(username, date, category, amount, description, trans_type)
        elif choice == '2':
            df = view_transactions(username)
            print(df)
        elif choice == '3':
            visualize_transactions(username)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
