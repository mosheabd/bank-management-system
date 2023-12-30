# bank_ui.py
from bank import Bank
from validations import validate_full_name, validate_email, validate_address, validate_phone_number, validate_birth_date
from database_manager import initialize_db


def create_account_ui(bank):
    print("\n--- Create New Account ---")
    while True:
        full_name = input("Enter full name: ")
        valid, message = validate_full_name(full_name)
        if valid:
            break
        print(message)

    while True:
        email = input("Enter email: ")
        valid, message = validate_email(email)
        if valid:
            break
        print(message)

    while True:
        address = input("Enter address: ")
        valid, message = validate_address(address)
        if valid:
            break
        print(message)

    while True:
        phone_number = input("Enter phone number: ")
        valid, message = validate_phone_number(phone_number)
        if valid:
            break
        print(message)

    while True:
        birth_date = input("Enter birth date (DD/MM/YYYY): ")
        valid, message = validate_birth_date(birth_date)
        if valid:
            break
        print(message)

    account = bank.create_account(full_name, email, address, phone_number, birth_date)
    print(f"Account created. Account Number: {account.account_number}, PIN: {account.pin}")


def transaction_ui(bank, transaction_type):
    print(f"\n--- {transaction_type.capitalize()} Money ---")
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    new_balance = None

    try:
        amount = float(input(f"Enter amount to {transaction_type}: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    if transaction_type == "deposit":
        new_balance = bank.deposit(account_number, pin, amount)
    elif transaction_type == "withdraw":
        new_balance = bank.withdraw(account_number, pin, amount)

    if new_balance is not None:
        print(f"Transaction successful. New balance: {new_balance}")
    else:
        print(f"Transaction failed. Check account details or balance.")


def check_balance_ui(bank):
    print("\n--- Check Account Balance ---")
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    balance = bank.check_balance(account_number, pin)
    if balance is not None:
        print(f"Account Balance: {balance}")
    else:
        print("Invalid account number or PIN.")


def close_account_ui(bank):
    print("\n--- Close Account ---")
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    account = bank.db_manager.get_account(account_number, pin)
    if not account:
        print("Invalid account number or PIN.")
        return

    confirmation = input("Are you sure you want to close this account? (Y/N): ").strip().upper()
    if confirmation == "Y":
        bank.close_account(account_number, pin)
        print("Account closed successfully.")
    else:
        print("Account closure cancelled.")


def main_menu(bank):
    menu_options = {
        "1": lambda: create_account_ui(bank),
        "2": lambda: transaction_ui(bank, "deposit"),
        "3": lambda: transaction_ui(bank, "withdraw"),
        "4": lambda: check_balance_ui(bank),
        "5": lambda: close_account_ui(bank),
        "0": lambda: print("Exiting system. Thank you for using our services.")
    }

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Balance")
        print("5. Close Account")
        print("0. Exit")
        choice = input("Enter your choice: ")

        action = menu_options.get(choice)
        if action:
            action()
            if choice == "0":
                break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    initialize_db()
    nu_bank = Bank()
    main_menu(nu_bank)
