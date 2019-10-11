#! Классы для book9.


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


class Restaurant:
    """
    Try it yourself 9-1
    Try it yourself 9-4
    """

    def __init__(self, resraurant_name, cuisine_type):
        """Initiazile name and type attributes"""
        self.restaurant = resraurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restraunt(self):
        print("Ресторан называется \"" + self.restaurant.title() + "\".")
        print("Тип кузин в нём: " + self.type + ".")
        print("Кужины обслужили " + str(self.number_served) + " клиентов." +
              "\n")

    def open_restraunt(self):
        print("Ресторан \"" + self.restaurant.title() + "\" открыт!")

    def set_number_seved(self, customers):
        """Set number of served customers"""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("Don't fuck with me son.")

    def increment_number_served(self, new_customers):
        """Increment of served cusomers"""
        if new_customers >= 0:
            self.number_served += new_customers
        else:
            print("Wise guy, heh? You are nothing but joke.")


class User:
    """Try it yourself 9-3"""

    def __init__(self, name, surname, age, sex, education):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.education = education
        self.login_attempts = 0

    def describe_user(self):
        print("Name:\t" + self.name.title() + "\nSurname:\t" +
              self.surname.title() + "\nAge:\t" + str(self.age) +
              "\nSex:\t" + self.sex + "\nEducation:\t" +
              self.education + "\nLogin:\t" + str(self.login_attempts) +
              "\n")

    def greet_user(self):
        print("Hello, " + self.name.title() + " " +
              self.surname.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You bastard can not roll back an odomtner!" + "\n" +
                  "Roll back your mama!")

    def increment_odometer(self, miles):
        """
        !!! 2-2 !!!
        Add the given amount to the odometer reading.
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Clever motherfucker! Fuck you!")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()    # Класс как атрибут.

    def get_descriptive_name(self):
        return (str(self.year) + ' ' + self.make + ' электромобиль ' +
                self.model)

    def fill_gas_tank(self):
        print(self.model.title() + " doesn't need a gas tank!")


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        """Try iy yourself 9-9"""
        if self.battery_size < 85:
            self.battery_size = 85

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        range = self.battery_size * 4
        print("This car can go approximately " + str(range) +
              " miles on a full charge.")
