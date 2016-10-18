def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

days = ('man', 'tir', 'ons', 'tor', 'fre', 'lor', 'son')

def weekday_newyear(year):
    sum_extra_leap_days = 0
    for i in range(1900, year):
        if is_leap_year(i):
            sum_extra_leap_days += 1
    # sum_extra_leap_days = sum(int(is_leap_year(i)) for i in range(1900, year))
    
    # first get the normal amount of days in a year, then add the total sum of extra leap days from the years before
    # then mod 7 to get int for the day
    return ((year - 1900) * 365 + sum_extra_leap_days) % 7

def is_workday(day):
    return day < 5

def workdays_in_year(year):
    s = 5 * 52 # minumum number of workdays
    if is_workday((weekday_newyear(year) + 364) % 7): s += 1 # if day 365 is a workday
    if is_leap_year(year) and is_workday((weekday_newyear(year) + 365) % 7): s += 1 # if leapyear and last day is workday
    return s # reutrn sum of workdays

# print stuff
for i in range(1900, 1920):
    print(i, days[weekday_newyear(i)], workdays_in_year(i))
