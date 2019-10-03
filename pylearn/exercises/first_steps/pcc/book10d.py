#! Занятие по книге Python Crash Course, chapter 10, "Files and
# Exceptions".  Занятие четвёртое.

# Try it yourself 10-6, 10-7.


def addition(x, y):
    while x != 'stop' or y != 'stop':
        try:
            print(int(x) + int(y))
        except ValueError:
            print("Value Error")
        x = input("Введите первое число (stop для выхода): ")
        if x == 'stop':
            break
        y = input("Введите второе число: ")
    return 'Stoped'


addition(5, 6)


# Try it yourself 10-8.


def cats_and_dogs(file):
    while file != 'stop':
        file = input("Введите путь к файлу (stop для выхода): ")
        try:
            with open(file) as file_obj:
                for line in file_obj:
                    print(line.strip())
        except FileNotFoundError:
            # pass (silent file is missing error).
            print("Friendly 'FileNotFoundError' message.")


cats_and_dogs('peep')


# Try it yourself 10-10.


def common_words():
    file = input("Введите путь к файлу: ")
    try:
        with open(file) as file_obj:
            lines = file_obj.read()
            print(lines.lower().count('терпеть'))
    except FileNotFoundError:
        pass


common_words()
common_words()
