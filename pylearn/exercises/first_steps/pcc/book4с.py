#! Книга "Python Crash Course", Глава 4. Working with Lists. Занятие 3.

my_food = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_food   # Здесь будет не копирование, а эквивалент.

my_food.append('cannoli')
friend_foods.append('ice cream')

print("Lists are equal: " + str(my_food) + "\n" + str(friend_foods))


slices = [numbers*2 for numbers in range(1, 10)]  # try-it-yourself 4.10
print("The first three items in the list are:\n" + str(slices[0:3]))
print("Three items in the middle of the list are\n" + str(slices[3:6]))
print("The last three items in the list are:\n" + str(slices[6:10]))


pizzas = ['pepperoni', 'margarita', 'four seas']   # try-it-yourself 4.11
friend_pizzas = pizzas[:]

pizzas.append('clouds in camarillo')
friend_pizzas.append('so unreal')

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")

for friend_pizza in friend_pizzas:
    print(friend_pizza.title())


food1 = ['can', 'cum', 'cel', 'cis']
food2 = ['ban', 'bum', 'bes', 'big']    # try-it-yourself 4-12

for food in food1:
    food2.append(food)
print("Full 2: ", food2)

# Tuples.  Не до конца понимаю смысл слова кортеж здесь.  Знаю про
# кортежи сопровождения.  Неизменяемые листы  .  Immutable.

dimensions = (200, 50)      # Immutable tuple - круглые скобочки.
print(dimensions[0], '\n', dimensions[1])

# dimensions[0] = 250       # Выдаст ошибку, низя изменить.
for dimension in dimensions:
    print(dimension)

print("Original dimensions:", dimensions[0], ",", dimensions[1])

dimensions = (400, 100)     # Переназначение целого кортежа.
print("\nModified dimensions:", dimensions[0], ",", dimensions[1])

# Конец занятия 3.
