import random as rnd
import datetime
import calendar
from decimal import Decimal, getcontext

getcontext().prec = 2


class Subscription:
    """
    Generate subscriptions expenses monthly for given period from start to end date.

    Attributes:


    """

    def __init__(
        self,
        id: str,
        value: Decimal,
        start_date: tuple[int, int],
        end_date: tuple[int, int],
        due_day: int,
    ):
        self.id = id
        self.value = value
        self.start_date = start_date
        self.end_date = end_date
        if not (1 <= due_day <= 25):
            raise ValueError("due day must be between 1 and 25")
        self.due_day = due_day

    def generate_subscriptions(self) -> list[dict]:
        """
        Generate monthly expense from subscription.

        Return:
            dict row with Id,Value and Date.
        """
        entry_date = datetime.date(self.start_date[0], self.start_date[1], self.due_day)
        end_date = datetime.date(self.end_date[0], self.end_date[1], self.due_day)
        if entry_date > end_date:
            raise ValueError("Start date must be before end date")
        current_date = entry_date
        subscription_entries = []
        while current_date <= end_date:
            current_year = current_date.year
            current_month = current_date.month

            row_entry = {
                "id": self.id,
                "value": self.value,
                "date": datetime.date(current_year, current_month, self.due_day),
            }
            subscription_entries.append(row_entry)

            if current_month == 12:
                current_year += 1
                current_month = 1
            else:
                current_month += 1
            current_date = datetime.date(current_year, current_month, self.due_day)

        return subscription_entries
