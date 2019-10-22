# This is a new Day File

class NewDay:
    counter = 0
    def __init__(self, phrase="Hurray!"):
        self.phrase = phrase
        NewDay.counter += 1

    def praise(self):
        return self.phrase + "!!!"

    def cry(self):
        return self.phrase + " :("

    def prime_factors(self, number):
        factors = [1]
        end = self.get_end(number)
        for i in range(2, end):
            if i > number:
                break
            while number % i == 0:
                factors.append(i)
                number /= i
        else:
            if number not in factors:
                factors.append(int(number))
        return factors

    @staticmethod
    def get_end(number):
        return int(number ** 0.5)

    @staticmethod
    def is_prime(number):
        end = self.get_end(number)
        for i in range(2, end):
            if number % i == 0:
                return False
        else:
            return True


day = NewDay()
print(day.counter, NewDay.counter)

print(day.praise(), day.cry())
print(day.prime_factors(1))
