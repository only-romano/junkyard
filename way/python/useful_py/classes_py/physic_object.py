"""PHISICS"""
class PhisicObject:
    """Just to remember all measures"""
    def __init__(self, mass=1, distance=1, time=1):
        self.mass = mass  # mass in kilogrames
        self.distance = distance  # distance in metres
        self.time = time  # time in seconds
        self.electrons = 6.241506e18
        self.mole = 6.022169e23
        self.cycles = 1

    def speed(self):
        # speed is metres per second
        return self.distance / self.time

    def force(self):
        # force is kilogram-metres per squared second, Newtons
        return self.mass * self.speed() / self.time

    def energy(self):
        # energy is kilogram-squared metres per squared seconds, Joule
        return self.force() * self.metres()

    def power(self):
        # power is kilogram-squared metres per cubed seconds, Watt
        return self.energy() / self.time

    def electric_current(self):
        # count of electrons per second, Ampere
        return self.electrons / (self.time * 6.241506e18)

    def electric_charge_quantity(self):
        # ECL is Amperes-second, Coulomb
        return self.electric_current() * self.time

    def electric_potential(self):
        # Electric potential or potential difference or electromotive force (EMF)
        # is equal to Joules per Coulumbs or
        # kilogram-squared metres per squared seconds-electrons, Volt
        return self.energy() / self.electric_charge_quantity()

    def electrical_resistance(self):
        # Volt per Ampere or
        # kilogram-squared metres * 6.241506e18 per seconds-squared electrons, Ohm
        return self.electric_potential() / self.electric_current()

    def frequency(self):
        # cycle per second
        return self.cycles / self.time


class Converter(PhisicObject):
    """Measures convertion"""
    def __init__(self, mass=1, distance=1, time=1):
        super(self, mass, distance, time)
        self.temperature = 273
        self.candela = 1

    def nanometers(self):
        return self.distance * 1e9

    def microns(self):
        return self.distance * 1e6

    def milimeters(self):
        return self.distance * 1e3

    def centimetres(self):
        return self.distance * 1e2

    def inches(self):
        return self.distance * 39.37

    def feet(self):
        return self.distance * 3.281

    def yards(self):
        return self.distance * 1.094

    def kilometres(self):
        return self.distance * 1e-3

    def statute_miles(self):
        return self.distance * 6.214e-4

    def nautical_miles(self):
        return self.distance * 5.397e-4

    def nanograms(self):
        return self.weight * 1e12

    def micrograms(self):
        return self.weight * 1e9

    def milligrams(self):
        return self.weight * 1e6

    def grams(self):
        return self.weight * 1e3

    def ounces(self):
        return self.weight * 35.28

    def pounds(self):
        return self.weight * 2.205

    def english_tons(self):
        return self.weight * 1.103e-3

    def minutes(self):
        return self.time * 0.01667

    def hours(self):
        return self.time * 2.778e-4

    def days(self):
        return self.time * 1.157e-5

    def years(self):
        return self.time * 3.169e-8

    def celsius(self):
        return self.temperature - 273

    def fahrenheit(self):
        return self.temperature * 1.8 - 459

    def rankine(self):
        return self.temperature * 1.8

    def carriers(self):
        return self.electric_current() * 6.24e18

    def nanoamperes(self):
        return self.electric_current() * 1e9

    def microamperes(self):
        return self.electric_current() * 1e6

    def milliamperes(self):
        return self.electric_current() * 1e3

    def microwatts_ster(self):
        return self.candela * 1.464e3

    def milliwatts_ster(self):
        return self.candela * 1.464

    def watts_ster(self):
        return self.candela * 1.464e-3

    def coulombs(self):
        return self.mole * 9.65e4


def speed(distance, time):
    return 

