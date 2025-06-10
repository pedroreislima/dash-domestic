from expense import Expense
from subscription import Subscription
import datetime

from decimal import Decimal, getcontext

getcontext().prec = 2

expenses_list = [
    ["Lamen", [Decimal(34.99), Decimal(19.99)], [0.3, 0.7], "constant"],
    ["Pizza", [Decimal(59.99), Decimal(30)], [0.4, 0.6], "wknd"],
    ["Feijoada", [Decimal(32.00), Decimal(24.99)], [0.5, 0.5], "constant"],
    ["Carangueijo", [Decimal(50.00)], [1], "quinta"],
    ["Ice cream", [Decimal(21)], [1], "wknd"],
]


def generate_table_expenses(expenses_list: list) -> list:
    """
    Generate expenses given monthly occurrences. Each input will help build 3 months for simplicity.
    """

    start_year = int(input("give the starting year in int"))
    start_month = int(input("give the starting month"))
    start_date = datetime.date(start_year, start_month, 1)

    end_year = int(input("give the ending year in int"))
    end_month = int(input("give the ending month"))
    end_date = datetime.date(end_year, end_month, 1)

    data = []
    for expense in expenses_list:
        print(f"now dealing with {expense[0]}")

        current_year = start_year
        current_month = start_month
        current_date = start_date
        while current_date <= end_date:
            occurrences = int(
                input(
                    f"how many ocurrences of {expense[0]} in {current_year, " ", current_month} and the next two months?"
                )
            )

            # generate 3 months of data
            for i in range(3):

                for j in range(occurrences):
                    entry = Expense(expense[0], expense[1], expense[2], expense[3])
                    data.append(entry.generate_expense(current_year, current_month))

                if current_month == 12:
                    current_year += 1
                    current_month = 1
                else:
                    current_month += 1
                current_date = datetime.date(current_year, current_month, 1)
    return data


def generate_subscriptions():
    pass


def generate_pontual_expenses():
    pass
