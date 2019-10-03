# Хорошей практикой является объявление всех функций в самом верху

# Функция-задание
def is_primal(number):
    y=1
    for i in range(2, number):
        if number % i == 0:
            y+=1
        if y>1:
            break
    x = y==1
    return x


# Функция которая тестирует is_primal
def test(num):
    print(num, ' ', is_primal(num))


# А теперь блок так называемых "тестов", это код который проверяет твою функцию
test(1)
test(7)
test(103)
test(14)
test(1001)
test(2017)
test(180)
