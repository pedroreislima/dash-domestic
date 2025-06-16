from expense import Expense
from subscription import Subscription
import datetime
import pandas as pd

from decimal import Decimal, getcontext

getcontext().prec = 2

expenses_list = [
    ["Lamen", [Decimal("34.99"), Decimal("19.99")], [0.3, 0.7], "constant"],
    ["Pizza", [Decimal("59.99"), Decimal("30")], [0.4, 0.6], "wknd"],
    ["Feijoada", [Decimal("32.00"), Decimal("24.99")], [0.5, 0.5], "constant"],
    ["Carangueijo", [Decimal("50.00")], [1], "quinta"],
    ["Ice cream", [Decimal("21")], [1], "wknd"],
]

fixed_behavior = [
    ["health insurance", (2024, 8), (2025, 6), Decimal(250), 15],
    ["health insurance", (2025, 7), (2025, 12), Decimal(300), 15],
    ["braces", (2024, 6), (2025, 6), Decimal(100), 5],
    ["gym", (2024, 1), (2024, 7), Decimal(70), 20],
    ["gym", (2024, 8), (2025, 3), Decimal(85), 20],
    ["gym", (2025, 6), (2025, 12), Decimal(85), 10],
    ["netflix", (2024, 1), (2025, 4), Decimal(25), 6],
    ["netflix", (2025, 5), (2025, 12), Decimal(35), 6],
    ["crunchyroll", (2024, 5), (2024, 8), Decimal(15), 6],
    ["crunchyroll", (2024, 11), (2025, 3), Decimal(15), 6],
    ["italian course", (2025, 6), (2025, 11), Decimal(320), 2],
]

pontual_expenses_list = [
    ["Drawing Tablet", [Decimal("1200")], [1], "constant", "2025-02-26"],
    ["Bike", [Decimal("750")], [1], "constant", "2024-02-26"],
]

pontual_expenses_list = [
    {"id": "Bike", "value": Decimal("750"), "date": datetime.date(2024, 2, 26)},
    {
        "id": "Drawing Tablet",
        "value": Decimal("1200"),
        "date": datetime.date(2025, 2, 26),
    },
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


def generate_subscriptions(subscription_list: list):
    data = []
    for subscription in subscription_list:
        entry = Subscription(
            subscription[0],
            subscription[3],
            subscription[1],
            subscription[2],
            subscription[4],
        )
        entry = entry.generate_subscriptions()
        # as it is a list of entries, we will extend the data so it can properly function.
        data.extend(entry)
    return data


def generate_pontual_expenses():
    pass


if __name__ == "__main__":
    dados = []
    # genereta tables!
    # expenses
    entry = generate_table_expenses(expenses_list)
    dados.extend(entry)
    # subscriptions
    entry = generate_subscriptions(fixed_behavior)
    dados.extend(entry)
    # add fixed behavior
    entry = pontual_expenses_list
    dados.extend(entry)
    # make dataframe and export csv
    dados = pd.DataFrame(dados)
    dados.to_csv(
        "/home/prlima/Documents/code/dash-domestic/data/grossdata.csv", encoding="utf-8"
    )
    pass
