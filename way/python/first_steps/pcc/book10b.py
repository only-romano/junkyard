#! Занятие по книге Python Crash Course, chapter 10, "Files and
# Exceptions".  Занятие второе.

# Try it yourself 10-1:

with open('../day/new.txt', 'r') as file_stuff:
    print(file_stuff.read())
    print(file_stuff)

with open('../day/new.txt', 'r') as file_stuff:
    for line in file_stuff:
        print(line.strip())

with open('../day/new.txt', 'r') as file_stuff:
    lines = file_stuff.readlines()

for line in lines:
    print(line.rstrip())


# Try it yourself 10-2:

for line in lines:
    print(line.replace('Python', 'Sex').rstrip())


# Writing to a file.

# Mode that allows you to read and write to the file : 'r+' .
# Разделители и табуляция работают в файлах.

with open('../day/programming.txt', 'r+') as file_stuff:
    file_stuff.write("I fucking love programming.\n")
    file_stuff.write("\tI damn love creating new games too cool for"
                     " this silly world!\n")

with open('../day/programming.txt', 'a') as file_stuff:
    file_stuff.write("I also love finding meaning in large pussies.\n")
    file_stuff.write("I love creating poo that can run in a toilet.\n")


# Try it yourself 10-3, 10-4:

with open('../day/guests.txt', 'w') as file_stuff:
    file_stuff.write("Guests:\n")


def guests():
    answer = input("Hello guest, what is your name?\n")
    with open('../day/guests.txt', 'a') as file_stuff:
        file_stuff.write(answer + '\n')
    print("Greetings, " + answer + '.')


answer = input("Do you wanna come into cicle?\tYes/No\n").lower()

while answer != 'no':
    answer = input("Do you wanna more?\tYes/No\n").lower()
    guests()


# Try it yourself 10-5:

while answer != 'fuck':
    answer = input("Why do you like programming?\t('fuck' for exit)")
    with open('../day/reasons.txt', 'a') as file_stuff:
        file_stuff.write('Reason: ' + answer + '\n')
