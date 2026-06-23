# random_test.py

import random
from datetime import datetime


class CoffeeOrder:
    def __init__(self, customer, drink):
        self.customer = customer
        self.drink = drink
        self.order_time = datetime.now()

    def summary(self):
        return (
            f"{self.customer} ordered a {self.drink} "
            f"at {self.order_time.strftime('%H:%M:%S')}"
        )


def generate_orders(count=5):
    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    drinks = ["Latte", "Espresso", "Mocha", "Americano", "Cappuccino"]

    orders = []

    for _ in range(count):
        order = CoffeeOrder(
            random.choice(names),
            random.choice(drinks)
        )
        orders.append(order)

    return orders


def main():
    print("Coffee Shop Simulator")
    print("-" * 25)

    orders = generate_orders()

    for order in orders:
        print(order.summary())

    total_sales = round(random.uniform(15, 50), 2)
    print(f"\nEstimated sales: ${total_sales}")


if __name__ == "__main__":
    main()
