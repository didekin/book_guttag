import calendar as cal


def usa_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


def canada_thanksgiving(year):
    month = cal.monthcalendar(year, 10)
    if month[0][cal.MONDAY] != 0:
        thanksgiving = month[1][cal.MONDAY]
    else:
        thanksgiving = month[2][cal.MONDAY]
    return thanksgiving


def shopping_days(year, thanksgiving, plusdays):
    """
    year a number >= 1941
    thanksgiving a function calculating the day of the month for a particular country
    plusdays the sum of the days in the (full) months between thanksgiving day and december.
    returns the number of days between U.S. Thanksgiving and Christmas in year
    """
    return 25 + (plusdays - thanksgiving(year))


print(shopping_days(2023, usa_thanksgiving, 30))
print(shopping_days(2023, canada_thanksgiving, 61))
