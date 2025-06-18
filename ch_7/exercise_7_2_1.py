import calendar as cal
import datetime as dt


def thanksgivig(year):
    month = list(cal.Calendar().itermonthdays(year, 11))
    daymonth = month[3] if month[3] > 0 else month[10]
    return dt.date(year, 11, daymonth)


def thanksgivig_canadian(year):
    month = list(cal.Calendar().itermonthdays(year, 10))
    daymonth = month[7] if month[0] > 0 else month[14]
    return dt.date(year, 10, daymonth)


def shopping_days(year):
    """year a number >= 1941
       returns the number of days between U.S. Thanksgiving and Christmas in year"""
    christmasdate = dt.date(year, 12, 25)
    return christmasdate - thanksgivig(2011)


def shopping_days_canadian(year):
    """year a number >= 1941
       returns the number of days between Canada Thanksgiving and Christmas in year"""
    christmasdate = dt.date(year, 12, 25)
    return christmasdate - thanksgivig_canadian(2011)


print(shopping_days(2011).days)
print(shopping_days_canadian(2011).days)

