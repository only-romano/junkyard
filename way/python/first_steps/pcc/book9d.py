#! Занятие по книге Python Crash Course, chapter 8, "Classes".
# Занятие четвёртое.
from classes_book9 import Car

# Переопределение методов родительских классов.
# Экземпляры как атрибуты.


class Battery:
    """A sumple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = self.battery_size * 4
        print("This car can go approximately " + str(range) +
              " miles on a full charge.")


class ElectricCar(Car):         # Родительский  класс в скобках
    """Represents aspects of a car, specific ti electuic vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)     # Связка классов.
        # !!! Python 2.7 !!!
        # super(ElectricCar, self).__init__(make, model year).
        self.battery = Battery()    # Класс как атрибут.

    def get_descriptive_name(self):
        """
        Можно переопределять методды родительского калсса, внимание
        будет на метод, что идёт в чайлд-классе.
        Return a neatly formatted descriptive name.
        """
        return (str(self.year) + ' ' + self.make + ' электромобиль ' +
                self.model)

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print(self.model.title() + " doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()


my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
