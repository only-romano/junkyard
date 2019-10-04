#! Простые задачки.


# Задача 1.  Дано трехзначное число.  Выведите на экран новое число,
# полученное из исходного путем перестановки цифр в обратном порядке.


def reverse_number(x):
    if len(str(x)) == 3:
        new_number = str(x)
        return int(new_number[::-1])
    pass


print(reverse_number(256))


# Задача 2.  Дано трехзначное число.  Замените среднюю цифру на ноль.


def midle_zero(x):
    if len(str(x)) == 3:
        new = list(str(x))
        new[1], b = '0', ''
        return int(b.join(new))
    pass


print(midle_zero(256))


# Задача 3.  Дано шестизначное число.  Поменяйте местами первую и
# последнюю цифры.


def num_exchange(x):
    if len(str(x)) == 6:
        new = list(str(x))
        b = [new[0], new[5]]
        new[0], new[5], b = b[1], b[0], ''
        return int(b.join(new))
    pass


print(num_exchange(256789))


# Задача 4.  Дано пятизначное число.  Цифры на четных позициях
# занулить.  Например, из 12345 получается число 10305.


def even_zero(x):
    if len(str(x)) == 5:
        new = list(str(x))
        new[1], new[3], b = '0', '0', ''
        return int(b.join(new))
    pass

print(even_zero(25678))

