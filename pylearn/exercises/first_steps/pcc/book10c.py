#! Занятие по книге Python Crash Course, chapter 10, "Files and
# Exceptions".  Занятие третье.

# Exceptions.

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# FUCKING CALCULATOR !

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        print(int(first_number) / int(second_number))
    except ZeroDivisionError:
        print("You can't divide by 0!")


# FileNotFoundError

try:
    with open('../alice.txt') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("Sorry, the file doesn't exist.")


# Analyzing Text


def count_words():
    """Count the approximate number of words in a file."""
    answer = input("Insert way to file: \n")
    try:
        with open(answer) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file doesn't exist.")
        # pass - Failing silently.
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The book has about " + str(num_words) + " words.")


while True:
    answer = input("Do you want to count words? \t(Yes/No)\n")
    if answer.lower() == 'no':
        break
    count_words()

