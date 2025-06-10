import datetime

# This file is for the functions used in the project.

# Step 0 Functions


def get_weekdays(year: int, month: int, week_day: int):
    """
    Get all specific days of week (ex. monday) from certain month and year.

    Return:
        list of dates on certain month
    """
    month_start = datetime.date(year, month, 1)
    start_date = month_start
    week_delta = week_day - month_start.weekday()
    if week_delta >= 0:
        start_date = month_start + datetime.timedelta(days=week_delta)
    if week_delta < 0:
        start_date = month_start + datetime.timedelta(days=week_delta + 7)

    # now we have the first date for that weekday, lets iterate until we are out of bounds on the month.
    iterate_date = start_date
    weekday_list = []
    while month_start.month == iterate_date.month:
        weekday_list.append(iterate_date)
        # print(iterate_date)
        iterate_date = iterate_date + datetime.timedelta(days=7)
    return weekday_list


# Step 1 Functions
