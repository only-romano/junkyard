#! Занятие по книге Python Crash Course, chapter 9, "Classes".
# Занятие третье.
from classes_book9 import Restaurant, User, Car

# Try-it-yourself 9-4.
my_pantyhouse = Restaurant("Pussycat", 'pussy')
my_pantyhouse.describe_restraunt()

my_pantyhouse.number_served = 1
my_pantyhouse.describe_restraunt()

my_pantyhouse.set_number_seved(3)
my_pantyhouse.set_number_seved(2)
my_pantyhouse.describe_restraunt()

my_pantyhouse.increment_number_served(2)
my_pantyhouse.increment_number_served(-1)
my_pantyhouse.describe_restraunt()

# Try-it-yourself 9-5.
new_user = User('sasha', 'severniy', 42, 'at least once', 'thug life')
new_user.describe_user()

x = 4
while x > 0:
    new_user.increment_login_attempts()
    x -= 1

new_user.describe_user()

new_user.reset_login_attempts()
new_user.describe_user()


# Наследование.

# child-класс не только наследует все атрибуты и методы из родительского
# класса, но и может инициировать новые атрибуты и методы собственно.


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
        self.barrery_size = 70

    def describe_barrary(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.barrery_size) + "-kWh.battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_barrary()


# Переопределение методов родительских классов.
# !!! fill gas tank !!!
