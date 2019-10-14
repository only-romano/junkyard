#! Занятие по книге Python Crash Course, chapter 11, "Testing your
# Code".  Занятие первое, задания.
# Try-it-yourself 11-1, 11-2.


def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


def city_functions(city, country, population=''):
    """Generate a neatly formatted city."""
    if population:
        return (city.title() + ', ' + country.title() + ' - population ' +
                str(population) + '.')
    return city.title() + ', ' + country.title() + '.'
