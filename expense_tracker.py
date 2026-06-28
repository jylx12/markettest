# expense_tracker.py

from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Expense:
    category: str
    description: str
    amount: float


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        self.expenses.append(
            Expense(category, description, amount)
        )

    def total_spent(self):
        return sum(expense.amount for expense in self.expenses)

    def totals_by_category(self):
        totals = defaultdict(float)

        for expense in self.expenses:
            totals[expense.category] += expense.amount

        return totals

    def print_report(self):
        print("=== Expense Report ===\n")

        for expense in self.expenses:
            print(
                f"{expense.category:<12}"
                f"{expense.description:<20}"
                f"${expense.amount:>7.2f}"
            )

        print("\nCategory Totals")
        print("-" * 35)

        for category, total in self.totals_by_category().items():
            print(f"{category:<12} ${total:.2f}")

        print("\nOverall Total")
        print("-" * 35)
        print(f"${self.total_spent():.2f}")


def main():
    tracker = ExpenseTracker()

    tracker.add_expense("Food", "Lunch", 14.75)
    tracker.add_expense("Transport", "Train Ticket", 3.50)
    tracker.add_expense("Shopping", "Notebook", 8.99)
    tracker.add_expense("Food", "Coffee", 5.25)
    tracker.add_expense("Entertainment", "Movie Ticket", 16.00)

    tracker.print_report()


if __name__ == "__main__":
    main()
