#! Занятие по книге Python Crash Course, chapter 11, "Testing your
# Code".  Занятие первое, код.


def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()


print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease guve me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
