from database_manager import DatabaseManager
import random


class BankAccount:
    def __init__(self, account_number, full_name, email, address, phone_number, birth_date, balance, pin):
        self.account_number = account_number
        self.full_name = full_name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.birth_date = birth_date
        self.balance = balance
        self.pin = pin


class Bank:
    def __init__(self):
        self.db_manager = DatabaseManager()

    def create_account(self, full_name, email, address, phone_number, birth_date):
        account_number = str(random.randint(10000, 99999))
        pin = str(random.randint(1000, 9999))
        new_account = BankAccount(account_number, full_name, email, address, phone_number, birth_date, 0, pin)
        self.db_manager.create_account(new_account)
        return new_account

    def deposit(self, account_number, pin, amount):
        account = self.db_manager.get_account(account_number, pin)
        if account:
            new_balance = account[6] + amount
            self.db_manager.update_balance(account_number, new_balance)
            return new_balance
        else:
            return None

    def withdraw(self, account_number, pin, amount):
        account = self.db_manager.get_account(account_number, pin)
        if account and account[6] >= amount:
            new_balance = account[6] - amount
            self.db_manager.update_balance(account_number, new_balance)
            return new_balance
        else:
            return None

    def check_balance(self, account_number, pin):
        account = self.db_manager.get_account(account_number, pin)
        if account:
            return account[6]
        else:
            return None

    def close_account(self, account_number, pin):
        account = self.db_manager.get_account(account_number, pin)
        if account:
            self.db_manager.delete_account(account_number)
