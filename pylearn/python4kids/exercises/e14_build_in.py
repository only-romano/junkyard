# Встроенные функции Python

# abs - модуль
steps = - 3
if abs(steps) > 0:  # 3 > 0
	print("двигается")


# bool - приведение к булевому значению
print(bool(0), bool(1), bool(-500), bool(None), bool('a'), bool(' '))
print(bool([]), bool([0]))

year = input("Год рождения: ")
if not bool(year.strip()):
    print("Вам следует ввести год рождения")

# dir и help - доступные функции класса
num = 1
print(dir(num))
print(help(num.conjugate))


# eval - исполнение кода из строки
your_calcs = input('Введите выражение: ')
print(eval(your_calcs))


# exec - исполнение более сложного кода из строки
my_prog = '''if 1 > 0:
    print("1 > 0")
'''
exec(my_prog)


# float - перобразование в вещественное число
print(float(12))
print(float("123.45678"))

your_age = input("Введите ваш возраст: ")
age = float(your_age)
if age > 13:
    print("Вы на %s лет старше чем положено" % (age - 13))


# int - преобразование в целое число
print(int(123.456))
print(int("123"))
# int("123.456")  - ValueError


# len - длина объекта
print(len("Это тестовая строка"))
creature_list = ["unicorn", "cyclop", "fairy", "elf", "dragon", "troll"]
print(len(creature_list))
enemies_map = {"Batman": "Joker", "Superman": "Lex Luthor", "Spiderman": "Green Goblin"}
print(len(enemies_map))

fruit = ["apple", "banana", "clemantine", "pataya"]
length = len(fruit)
for i in range(length):
    print("Фрукт с индексом %s: %s" % (i, fruit[i]))


# max и min - наибольшее и наименьшее значение
numbers = [5, 4, 10, 30, 22]
print("Min = %s, Max = %s" % (min(numbers), max(numbers)))
print(max("StringSTRING"))
print(max(1, 5, 10, 300, 450, 50, 90))

guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
    print("Бабах! Вы проиграли.")
else:
    print("Вы победили!")


# range - итератор в заданном диапазоне
for x in range(5):
    print(x, end=" ")
print(range(5), list(range(5)))


# sum - возвращает сумму списка
print(sum(list(range(15))))


# open - открывает файл для чтения или записи
test_file = open('test.txt', 'w')
test_file.write("Это текстовый файл")
test_file.close()

test_file = open('test.txt')
from_file = test_file.read()
test_file.close()
print(from_file)


# Упражнение 1 (глава 9)
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)
