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

    def nanometers(self):
        return self.distance * 1e9

    def microns(self):
        return self.distance * 1e6

    def millimeters(self):
        return self.distance * 1e3


def speed(distance, time):
    return 

