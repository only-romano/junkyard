#! Книга "Python Crash Course", Глава 4. Working with Lists. Занятие 2.

digits = list(range(1, 111))     # Ура, новые операнды
min(digits)     # Comprehensions = охват, понимание, включение
max(digits)
sum(digits)

# Как правильно перевести List Comprehensions?  Ты штука что ты тогда.
squares = [value**2 for value in range(1, 11)]
print(squares)      # Сочетает в себе цикл и команды в 1 строке.

for count20 in range(1, 21):        # try-it-yourself 4.3
    print(count20)

million = [mil for mil in range(1, 1000001)]
print(million)          # try-it-yourself 4.4
print(min(million))        # try-it-yourself 4.5
print(max(million))
print(sum(million))     # 500000500000 - забавно.

odd = []        # try-it-yourself 4.6
for od in range(1, 20, 2):
    print(od)
    odd.append(od)
print(odd)

multi = [number*3 for number in range(3, 31)]
print(multi)        # try-it-yourself 4.7

cube1 = []        # try-it-yourself 4.8
for number1 in range(1, 11):
    print(number1)
    cube1.append(number1**3)
print(cube1)

cube =[number2**3 for number2 in range(1, 11)]
print(cube)        # try-it-yourself 4.9

print(cube[0:3])    # Называется slice, работает как range по индексам
print(multi[1:4])
print(cube[:4])     # При отсутствии первого аргумента стартует с начала
print(odd[6:])      # Соответственно без последнего идёт до окончания.
print(odd[-4:])     # Четвёртый с конца и до конца.

print("Here are the first three numbers in my range:")
for square in squares[:3]:  # Хотела спросить - как сортировать,
    print(square)   # вспомнила про .sort() и sort().

my_food = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_food[:]   # Пример копирования списков.

print("My favorite foods are: " + str(my_food) + ".")
print("\nMy friend's favorite foods are: " + str(friend_foods) + ".")

my_food.append('cannoli')       # Доказательство отдельности списков.
friend_foods.append('ice cream')
print("Different lists: " + str(my_food) + "\n" + str(friend_foods))