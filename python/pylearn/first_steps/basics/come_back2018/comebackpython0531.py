import base64, time, calendar, os, sys


class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    if age in range(1, 100):
      self.__age = age
    else:
      print("Wrong value")

  @property
  def name(self):
    return self.__name

  def display_info(self):
    print("Name:", self.__name, "\tAge:", self.__age)


kato = Person("Kato", 27)

kato.display_info()
kato.age = 28
kato.display_info()


class Employee(Person):

  def __init__(self, name, age, company):
    Person.__init__(self, name, age)
    self.company = company

  def display_info(self):
    Person.display_info(self)
    print(self.name, "works in company", self.company)


kato = Employee("Kato", 27, "Home")
kato.display_info()

Str = 'alalalalalala'
Str1 = base64.b64encode(Str.encode('utf-8', errors='strict'))
Str2 = base64.b64decode(Str1.decode('utf-8', errors='strict'))
print(Str, Str1, Str2)



class Employee2:
  "Base employee"
  empCount = 0
  __secretCount = empCount

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee2.empCount += 1
    Employee2.__secretCount += 2

  def displayCount(self):
    print("Total Employee %d" % Employee2.empCount)

  def displayInfo(self):
    print("Name:", self.name, ";\tSalary:", self.salary)


emp1, emp2 = Employee2("Katty", 4000), Employee2("Sana", 2000)
emp1.displayInfo()
emp2.displayCount()
print(emp2._Employee2__secretCount)  # Secret parameter
