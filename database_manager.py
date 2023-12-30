import sqlite3


class DatabaseManager:
    def __init__(self):
        self.db_file = 'bank_system.db'

    def create_account(self, account):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (account.account_number, account.full_name, account.email,
                            account.address, account.phone_number, account.birth_date,
                            account.balance, account.pin))
            conn.commit()

    def update_balance(self, account_number, new_balance):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?",
                           (new_balance, account_number))
            conn.commit()

    def get_account(self, account_number, pin):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM accounts WHERE account_number = ? AND pin = ?"
            params = (account_number, pin)
            cursor.execute(query, params)
            return cursor.fetchone()

    def delete_account(self, account_number):
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
            conn.commit()


def initialize_db():
    connection = sqlite3.connect('bank_system.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            balance REAL NOT NULL,
            pin TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_db()
