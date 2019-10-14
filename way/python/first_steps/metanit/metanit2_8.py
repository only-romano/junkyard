#!Учебный код по программе Метанит, Глава 2, часть 8. Функция.
def say_hello():#простейшая функция без параметров, для вызова функции написать её название и параметры.
    print("hello")
say_hello()

def greet(name):#функция с параметром
    print("hello,", name)#запомнить - запятая даёт пробел, плюсик нет.
greet('zhenya')
greet('kato')

def default_greet(name ="kato"):#функция с параметром по-умолчанию.
    print("hello", name)
default_greet()
default_greet('zhenya')

def info(name="kato", age=12):#функция с двумя именными параметрами, а также значением по умолчанию.
    print("Name:", name.title(), "\t", "Age:", age)
info()
info('zhenya', 24)
info(name="Vova", age=32)#примеры работы с параметрами функции.

def exchange(usd, money):#практика функции с возвратом.
    x = round(money/usd, 2)
    return x
result1=exchange(60, 3000)
print(result1)
result2=exchange(57, 252000)
print(result2)

def quatro(y):#функция, что возвращает несколько значений.
    sq=y**2
    tr=y**3
    qu=y**4
    return sq, tr, qu
square, tripple, quatro = quatro(2)
print("Sq=", square, "\t", "Tr=", tripple, "\t", "Qu=", quatro)

def main():#главная исполяющая функция, что объединяет исполнение других мелких функций, для упорядочивания
    say_hello()
    greet('zhenya')
    default_greet()
    info('vova', 32)
    print("К выдаче:", exchange(55, 2000), "долларов.")
    print("Sq=", square, "\t", "Tr=", tripple, "\t", "Qu=", quatro)
main()