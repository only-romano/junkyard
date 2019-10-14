#! Занятие по книге Python Crash Course, chapter 8, "Classes".
# Занятие шестое.

from classes_book9 import Car, ElectricCar, Battery
import restraunt
from users import *

my_new_car = Car('audi', 's5', 2017)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_huesla = ElectricCar('huesla', 'model xyu', 2017)

print(my_huesla.get_descriptive_name())
my_huesla.battery.describe_battery()
my_huesla.battery.get_range()


# Try it yourself 9-10.

zaibala = restraunt.Restaurant("Fuck you", "FUUUUUCK")
zaibala.describe_restraunt()


# Try it yourself 9-11, 9-12.

bobby = User('Shit', 'hole', 22, 'ass', 'suck dicks')
michael = Admin('Mike', 'duck', 23, 'stoned', 'harvard')
michael.priviliges.show_privileges()
