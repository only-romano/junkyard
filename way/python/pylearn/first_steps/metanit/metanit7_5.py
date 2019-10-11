#! Работа с материалами Metanit, глава 7, часть 5.  Класс object.
# Строковое представление объекта.

# Начиная с 3-й версии Python все классы неявно имеют один общий
# суперкласс - object и все классы по умолчанию наследуют его методы.


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 133):
            self.__age = age
        else:
            print("Недопустимый возраст")

    # Метод __str__() должен возвращать строку.  И в данном случае мы
    # возвращаем базовую информацию о человеке.  И теперь консольный
    # вывод будет другим:

    def __str__(self):
        return "Имя: {} \t Возраст: {}".format(self.__name, self.__age)

    def display_info(self):
        print(self.__str__())


tom = Person("Tom", 23)
print(tom)
