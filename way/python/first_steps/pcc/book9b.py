#! Занятие по книге Python Crash Course, chapter 9, "Classes".
# Занятие второе.


class Car:
    """A simple attempt to represent a car."""

    # Каждый атрибут в классе нужно инициировать, даже если значение
    # пустое или 0.  В некоторых случаях, например, когда надо выставить
    # значение по-умолчанию - имеет смысл инициировать атрибут в теле
    # __init__() метода.  Если сделать это для атрибута, необязательно
    # указывать параметр для этого атрибута.

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # Атрибут со значением по-умолчанию.
        self.gas_tank = 60

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return str(self.year) + ' ' + self.make + ' ' + self.model

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        !!! 1 !!!
        Set the odometer reading to the given value.  Reject the change
        if it attempts to roll odometer back.
        """
        if self.gas_tank > 0:
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
                self.gas_tank -= mileage / 12
        else:
            print("You bastard can not roll back an odomtner!" + "\n" +
                  "Roll back your mama!")

    def increment_odometer(self, miles):
        """
        !!! 2-2 !!!
        Add the given amount to the odometer reading.
        """
        if self.gas_tank > 0:
            if miles >= 0:
                self.odometer_reading += miles
                self.gas_tank -= miles / 12
        else:
            print("Clever motherfucker! Fuck you!")

    def fill_gas_tank(self, litres):
        """Fiils the gas tank"""
        if litres >= 0:
            self.gas_tank += litres
        else:
            print("Fuck you")

    # Как только Python вызовет метод __init__(), чтобы создать новый
    # инстансе - инициируется новый атрибут со значением 0.


my_new_car = Car('mazda', 'millenia', 1998)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Изменение значений атрибутов.

# Изменять значения можно тремя путями
# - напрямую через инстанс;
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# - задать значение через метод (!!! 1 !!!).
my_new_car.update_odometer(35)
my_new_car.read_odometer()
my_new_car.update_odometer(22)

# - прирастить значение в методе (!!! 2-2 !!!).
my_used_car = Car('mercedes', 'c200', 2001)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(158)
my_used_car.read_odometer()

# Можно использовать такие методы, чтобы контролировать как пользователи
# изменяют значения атрибутов, но любой с доступом к программе сможет
# изменить этот атрибут напрямую. Эффективная защита заключается в
# большом внимании к деталям в добавлениях к базовым проверкам.
