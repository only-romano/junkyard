#! Работа с материалами Metanit, глава 7, часть 4.  Полиморфизм.

# Полиморфизм является еще одним базовым аспектом ооп и предполагает
# способность к изменению функционала, унаследованного от базового
# класса.  Например, пусть у нас будет следующая иерархия классов:


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        if age in range(1, 133):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)


class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        # Обращение к методам базового класса имеет
        # следующий синтаксис:
        Person.__init__(self, name, age)
        # Employee добавляет к функционалу класса Person еще
        # один атрибут:
        self.company = company

    # переопределение метода display_info
    def display_info(self):
        # чтобы повторно не писать код вывода имени и возраста здесь
        # также происходит обращение к методу базового класса -
        # методу get_info:
        Person.display_info(self)
        print("Компания:", self.company)


class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)


people = [Person("Tom", 23), Student("Bob", 19, "Harvard"),
          Employee("Sam", 35, "Google")]

# На этапе выполнения программы Python учитывает иерархию
# наследования и выбирает нужную версию метода display_info()
# для каждого объекта.

for person in people:
    person.display_info()
    print()


# Проверка типа объекта.

# При работе с объектами бывает необходимо в зависимости от их
# типа выполнить те или иные операции.  И с помощью встроенной
# функции isinstance() мы можем проверить тип объекта.  Эта функция
# принимает два параметра:

# isinstance(object, type)

# Первый параметр представляет объект, а второй - тип, на
# принадлежность к которому выполняется проверка.  Если объект
# представляет указанный тип, то функция возвращает True.  Например,
# возьмем выше описанную иерархию классов:

for person in people:
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
    print()
