# Хорошей практикой является объявление всех функций в самом верху

# Функция-задание
def is_primal(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_primal2(numberz):
    for i in range(2, numberz):
        if numberz % i == 0:
            return False
    return True


# Функция которая тестирует is_primal
def test(num):
    print(num, ' ', is_primal(num))


# А теперь блок так называемых "тестов", это код который проверяет твою функцию


if __name__ == "__main__":      # Зачем это в основном файле программы?
    test(1)
    test(7)
    test(103)
    test(14)
    test(1001)
    test(2017)
    test(180)