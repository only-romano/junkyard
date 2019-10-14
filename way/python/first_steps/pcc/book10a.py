#! Занятие по книге Python Crash Course, chapter 10, "Files and
# Exceptions".  Занятие первое.
import math

# Из файла возвращаются данные в формате строк, для работы с другими
# типами требуется перевод в другой тип.

sexy = '../day/sexy.txt'
with open(sexy, 'w') as file_object:
    file_object.write(str(round(math.pi, 20)))

with open(sexy, 'r') as file_object:
    print(file_object.read().rstrip())
    # Метод rstrip() позволяет избежать лишней пустой строки в выводе.

with open(sexy, 'a') as file_object:
    file_object.write('\nsexy')

with open(sexy, 'r') as file_object:
    for line in file_object:
        print(line)


# Работа с контентом файла.

with open(sexy, 'a') as file_object:
    file_object.write('\n238462643383279')

with open(sexy) as file_object:
    lines = file_object.readlines()  # Создание листа из строк файла.

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    try:
        float(line)
        pi_string += line.rstrip()
    except Exception:
        pass

print("\n" + pi_string + "\n" + str(len(pi_string)))


# Объёмные файлы.

with open('../day/pi_1000.txt') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip().replace(' ', '')

print(pi_string[:52] + '...')   # Обрубочек файлика.
print(len(pi_string))


# Is my birthday in Pi?

def birthday_in_pi():
    birthday = input("Введите день, месяц своего рождния: ")
    birthday_number = []
    for symbol in birthday:
        if ord(symbol) in range(48, 57):
            birthday_number.append(symbol)
        else:
            pass
    num = ''.join(birthday_number)
    if num in pi_string:
        print("Днюха в пи." + num)
    else:
        print("Нет днюхи в пи.")


birthday_in_pi()


# Try it yourself 10-1, 10-2:

