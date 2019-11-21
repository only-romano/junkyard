from random import sample, randint
"""
Randomizer for available lists
plus radio broadcasting randomizer
"""
# Available lists randomizer class
class Randomize_and_pop_on_call:
    """
    Randomize given array and on call pop given value from array.
    If array is empty - returns None
    """
    # created only to ease-up code a little
    def __init__(self, array):
        self.array = sample(array, len(array))
    def __call__(self):
        return self.array.pop() if len(self.array) else None
# alias
randomize = Randomize_and_pop_on_call


# random radio
broadcast = "Евгеника" if randint(1, 4) == 1 else "Маяк"


__all__ = ['randomize', 'broadcast']

if __name__ == '__main__':
    # randomizer check
    ar = randomize([1,2,3,4,5])
    print(ar(), ar(), ar(), ar(), ar(), ar())
