#! Занятие по книге Python Crash Course, chapter 8, "Classes".
# Занятие пятое.
from classes_book9 import Restaurant, User, Car


class IceCreamStand(Restaurant):
    """Try it yourself 9-6."""
    def __init__(self, resraurant_name, cuisine_type):
        super().__init__(resraurant_name, cuisine_type)
        self.flavor = ['chocolate', 'vanilla']

    def set_flavor(self, flavor='chocolate'):
        if flavor not in self.flavor:
            self.flavor.append(flavor)
        return self.flavor

    def display_flavor(self):
        print("Available flavors are: " + ' '.join(i for i in self.flavor) +
              ".")


pied = IceCreamStand('Creamy pies', 'ice-hearted')
pied.set_flavor('orange juicy')
pied.display_flavor()


class Privileges:
    """Try iy yourself 9-8"""
    def __init__(self):
        """Initialize the battery's attributes."""
        self.privileges = ('can add post', 'can delete post',
                           'can ban user', 'can fuck your mama')

    def show_privileges(self):
        print("Admin can: " + ', '.join(i for i in self.privileges) + ".")


class Admin(User):
    """Try iy yourself 9-7"""
    def __init__(self, name, surname, age, sex, education):
        super().__init__(name, surname, age, sex, education)
        self.priviliges = Privileges()

    def describe_user(self):
        print("Name:\t" + self.name.title() + "\nSurname:\t" +
              self.surname.title() + "\nAge:\t" + str(self.age) +
              "\nSex:\t" + self.sex + "\nEducation:\t" +
              self.education + "\nLogin:\t" + str(self.login_attempts) +
              "\n" + "And this is fucking ADMIN!!!" + "\n")


serj = Admin("Serj", "Me", 27, "love it", "stupid")

serj.increment_login_attempts()
serj.greet_user()
serj.increment_login_attempts()
serj.describe_user()
serj.priviliges.show_privileges()


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


pussy_car = ElectricCar('Ridj', 'Pussyride', 2017)
pussy_car.battery.get_range()

pussy_car.battery.upgrade_battery()
pussy_car.battery.get_range()
