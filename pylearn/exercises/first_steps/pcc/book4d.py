#! Книга "Python Crash Course", Глава 4. Working with Lists. Занятие 4.

# try-it-yourself 4.13.a
buffet = ('soup', 'beef', 'coffee', 'tea', 'pancakes')
for food in buffet:
    print(food)

# try-it-yourself 4.13.b
try:
    buffet[3] = 'poop'
except Exception as e:
    print("\nОшибка: ", e)

# try-it-yourself 4.13.c
print("\nThe restaurant changes its menu\n")

buffet = ('tequila', 'beef', 'coffee', 'absent', 'paincakes')
for food in buffet:
    print(food)

# Styling the Code.