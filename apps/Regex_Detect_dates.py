# detect dates in the DD/MM/YYYY format. 
# Assume that the days range from 01 to 31, the months range from 01 to 12, 
# and the years range from 1000 to 2999. Note that if the day or month is a single digit, it will have a leading zero.
# February has 28 days
# February has 29 days in leap years. 
# Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 

import re

date_to_search = input('Enter a valid date in the DD/MM/YYYY format. ')

def IsValidDate(date_to_search):
    search = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)').search(date_to_search)
    try: 
        day = int(search.group(1))
        month = int(search.group(2))
        year = int(search.group(3))
    except (ValueError, AttributeError):
        quit('Error: Enter date in the DD/MM/YYYY format.')

    if day < 1 or month < 1 or month > 12:
        quit('Error: Enter a valid date in the DD/MM/YYYY format.')
    if year < 1000 or year > 2999:
        quit('Valid years are 1000 to 2999.')
    thirty_day_months = {4:'April',9:'September',11:'November'}
    thirtyone_day_months = {1:'January',3:'March',5:'May',6:'June',7:'July',8:'August',10:'October',12:'December'}
    if month in thirty_day_months.keys():
        if day > 30:
            quit(thirty_day_months[month]+' has 30 days. Enter a valid date in the DD/MM/YYYY format.')
    elif month == 2:
        # handle feb code here
        if year % 4 == 0 and year % 400 == 0:
            if day < 1 or day > 29:
                quit(str(year)+' is a leap year, in which February has only 29 days. Enter a valid date in the DD/MM/YYYY format')
        elif year % 4 == 0 and year % 100 == 0:
            if day <1 or day > 28:
                quit('In {}, February has only 28 days. Enter a valid date in the DD/MM/YYYY format'.format(str(year)))
        elif year % 4 == 0:
            if day < 1 or day > 29:
                quit(str(year)+' is a leap year, in which February has only 29 days. Enter a valid date in the DD/MM/YYYY format')
        else:
            if day < 1 or day > 28:
                quit('In {}, February has only 28 days. Enter a valid date in the DD/MM/YYYY format'.format(str(year)))
    else:
        # handle months with 1-31 days here
        if day > 31:
            quit(thirtyone_day_months[month]+' has 31 days. Enter a valid date in the DD/MM/YYYY format.')

IsValidDate(date_to_search)
