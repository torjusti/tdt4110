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
    return ((year - 1900) * 365 + sum(int(is_leap_year(i)) for i in range(1900, year))) % 7

def is_workday(day):
    return day < 5

def workdays_in_year(year):
    s = 5 * 52 # min amount
    if is_workday((weekday_newyear(year) + 364) % 7): s += 1
    if is_leap_year(year) and is_workday((weekday_newyear(year) + 365) % 7): s += 1
    return s

for i in range(1900, 1920):
    print(i, days[weekday_newyear(i)], workdays_in_year(i))
