#! Занятие по книге Python Crash Course, chapter 8, "Classes".
# Занятие седьмое.

from collections import OrderedDict
# Позволяет сохранять порядок ключей в словарях.
from random import randint
# Генерерует рандомные циферки в заданном рэндже.

# The Python Standard Library.

favorite_languanes = OrderedDict()
# Создаёт пустой упорядоченный словарь.

favorite_languanes['jen'] = 'python'
favorite_languanes['sarah'] = 'c'
favorite_languanes['edward'] = 'ruby'
favorite_languanes['phil'] = 'python'

for name, language in favorite_languanes.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
# Порядок всегда будет сохранён в упорядоченном словаре.


# Try it yourself 9-13.

terms = OrderedDict({'dictionary': 'thery cool stuff to store data',
                     'bug': 'shitty shit of whole shitness',
                     'method': 'tools to do some tangs',
                     'statement': 'something that is true or false',
                     'variable': 'store cells to little data :)'})

terms['loop'], terms['value'] = 'cicle of poo', 'data'

for term, meaning in terms.items():
    print(term.title(), "is a", meaning)


# Try it yourself 9-14.


class Die:

    def __init__(self, sides=6):
        """Represent rolling dices"""
        self.sides = sides

    def roll_die(self):
        print("Dice shows " + str(randint(1, self.sides)) + ".")


x, dice = 0, Die()
while x < 10:
    dice.roll_die()
    x += 1

dice = Die(10)
while x < 20:
    dice.roll_die()
    x += 1

dice = Die(20)
while x < 30:
    dice.roll_die()
    x += 1
