# mini_bank.py

import random
from datetime import datetime


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("deposit", amount, datetime.now()))

    def withdraw(self, amount):
        if amount > self.balance:
            self.transactions.append(("failed withdrawal", amount, datetime.now()))
            return False

        self.balance -= amount
        self.transactions.append(("withdrawal", amount, datetime.now()))
        return True

    def print_statement(self):
        print(f"\nAccount owner: {self.owner}")
        print(f"Current balance: ${self.balance:.2f}")
        print("\nTransactions:")

        for kind, amount, time in self.transactions:
            print(f"- {kind.title()}: ${amount:.2f} at {time.strftime('%H:%M:%S')}")


def main():
    account = BankAccount("Test User", 100)

    for _ in range(5):
        amount = round(random.uniform(5, 50), 2)

        if random.choice([True, False]):
            account.deposit(amount)
        else:
            account.withdraw(amount)

    account.print_statement()


if __name__ == "__main__":
    main()
