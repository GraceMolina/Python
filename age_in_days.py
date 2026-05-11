"""
calculating the age of a person in days
"""

import datetime

def days_in_month(year, month):
    """
    This function takes a year and a month as arguments. It returns the number 
    of days in the given month.
    """
    if year == 9999 and month == 12:
        return 31
    elif month == 12:
        date1 = datetime.date(year + 1, 1, 1) - datetime.date(year, month, 1)
        return date1.days
    else:
        difference = datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)
        return difference.days

def is_valid_date(year, month, day):
    """
    This function takes the arguments year, month, and day, which together form a date. 
    It returns True if the date is valid and False if it is invalid.
    """
    if year == 9999 and month == 12 and day == 31:
        return True
    else:
        valid_day_rage = days_in_month(year, month)
        return datetime.MINYEAR <= year <= datetime.MAXYEAR and 1 <= month <= 12 and 1 <= day <= valid_day_rage 

def days_between(year1, month1, day1, year2, month2, day2):
    """
    This function takes two dates as arguments. Specifically, the arguments year1, month1, 
    and day1 constitute an earlier date, while the arguments year2, month2, and day2 constitute 
    a later date. The function returns the number of days between these dates. If either date 
    is invalid or if the second date is earlier than the first, the function returns zero.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date1 <= date2:
            diff = date2 - date1
            return diff.days
        else: 
            return 0
    else:
        return 0

def age_in_days(year, month, day):
    """
    This function takes a birthday date as an argument. The arguments year, month, and day 
    constitute the birthday date. Given the birthday date, this function returns the age in 
    days. It returns 0 if the date is invalid or is a future date.
    """
    todays_date = datetime.date.today()
    if is_valid_date(year, month, day):
        date1 = datetime.date(year, month, day)
        if date1 <= todays_date:
            days = days_between(year, month, day, 
                                todays_date.year, 
                                todays_date.month, 
                                todays_date.day)
            return days
        else:
            return 0
    else:
        return 0

# calculate age in days
print(age_in_days(1993, 4, 3))
