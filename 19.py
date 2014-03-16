#!/usr/bin/python

tally = 0

def isleapyear(year):
    if year % 4 != 0:
        return False
    if year % 1000 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def increment(day, date, month, year):

    isleap = isleapyear(year)

    day += 1
    if day == 7: 
        day = 0

    date += 1
    if date == 32 and (month in [1, 3, 5, 7, 8, 10]):
        date = 1
        month += 1
    elif date == 32 and month == 12:
        date = 1
        month = 1
        year += 1
    elif date == 31 and (month in [9, 4, 6, 11]):
        date = 1
        month += 1
    elif date == 29 and month == 2 and isleap == False:
        date = 1
        month += 1
    elif date == 30 and month == 2 and isleap == True:
        date = 1
        month += 1

    return (day, date, month, year)

if __name__ == "__main__":

    ''' 0 = Sunday, 1 = Monday ... 6 = Saturday '''

    day = 1
    date = 1
    month = 1
    year = 1900

    while year < 2002:
        (day, date, month, year) = increment(day, date, month, year)
        if day == 0 and date == 1:
            if year > 1900 and year < 2001:
                tally += 1

    print tally
