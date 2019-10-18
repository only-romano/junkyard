class Converter:
    def __init__(self, weight=1, distance=1, time=1, temperature=273):
        self.distance = distance
        self.weight = weight
        self.time = time
        self.temperature = temperature
        self.current = 1
        self.candela = 1
        self.moles = 1

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
        return self.current * 6.24e18

    def nanoamperes(self):
        return self.current * 1e9

    def microamperes(self):
        return self.current * 1e6

    def milliamperes(self):
        return self.current * 1e3

    def microwatts_ster(self):
        return self.candela * 1.464e3

    def milliwatts_ster(self):
        return self.candela * 1.464

    def watts_ster(self):
        return self.candela * 1.464e-3

    def coulombs(self):
        return self.moles * 9.65e4


print(1e2)
