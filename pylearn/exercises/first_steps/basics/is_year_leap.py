#! The function 'is_year_leap' taking 1 argument - year, and returning
# True if the year is leap, and False differently.


def is_year_leap(year):
    """Determines whether a year is a leap year"""
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_year_leap(1967))
    print(is_year_leap(2008))
