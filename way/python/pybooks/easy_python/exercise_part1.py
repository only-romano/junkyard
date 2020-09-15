from pprint import pprint

# ex 1
seconds_per_hour = 60*60
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day/seconds_per_hour == seconds_per_day//seconds_per_hour)


# ex 2
s1 = { 1, 2, 3, 4, 5, 6 }
se = { 0, 2, 4, 6, 8 } 
so = { 1, 3, 5, 7, 9 }

print(s1 & so)
print(s1 | so)
print(s1 ^ so)
print(s1 >= so, s1 <= so, s1 > so, s1 < so)
print(s1|so >= so, s1 <= se|so)


# ex 3
years_list = range(1990, 1996)
third_bday = years_list[3]
print(third_bday)
print(max(years_list))

things = ['mozzarella', 'cinderella', 'salmonella']
print(things[1].capitalize(), things)
print(things[0].upper(), things)
things.remove('salmonella')
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise[-1].lower())
print(surprise[-1][::-1].lower().capitalize())


# ex 4
en2fr = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse",
}

print(en2fr["walrus"])

fr2en = {v: k for k, v in en2fr.items()}
print(fr2en["chien"])
print(set(en2fr))


life = {
    'animals': {
        'cats': [ "Henri", "Grumpy", "Lucy" ],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}
print(*life.keys())
print(*life['animals'].keys())
print(*life['animals']['cats'])


# ex 5
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

i = 10
while i:
    i -= 1
else:
    print("The're is no break in cycle")


# ex 6
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
deserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, desert in zip(days, fruits, drinks, deserts):
    print(f'{day}: drink {drink} eat {fruit} enjoy {desert}')

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list(zip(english, french)))
print(dict(zip(english, french)))


# ex 7
cells = [(x, y) for x in range(8) if x % 2 for y in range(8) if not y % 2 and x > 2]
pprint(cells)


# ex 8
def answer() -> None:
    print(42)

def run_smth(func: callable) -> None:
    func()

def add_args(*args) -> None:
    print(sum(args))

def run_smth_with_args(func: callable, *args) -> None:
    func(*args)

run_smth_with_args(add_args, 5, 9, 10, 3)


# ex 9 ЗАМЫКАНИЕ
def knights2(saying: str) -> callable:
    def inner2():
        return "We are the knights who say: %s" % saying
    return inner2


# ex 10 YIELD FUNCTION
def my_range(first:int=0, last:int=10, step:int=1) -> iter:
    number = first
    while number < last:
        yield number
        number += step

string = ""
for i in my_range():
    string += str(i)
print(string)


# ex 11 DECORATOR
def document_it(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> 'function call':
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return wrapper

def square_it(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return wrapper

@square_it
@document_it
def add_ints(*args) -> int:
    return sum(args)

print(add_ints(5,6,7, 15))


# ex 12 global variables
x, y, z = 12, 13, 15

def func():
    global x, y, z
    x *= 2
    y *= 3
    z *= 4

func()
print(x, y, z)


# ex 13 manual exceptions
class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
try:
    for word in words:
        if word.isupper():
            raise UppercaseException(word)
except UppercaseException as err:
    print(f'Error occured: {err}')


# ex 14
from random import randint
guess_me = 7

def guess_try(guess: int) -> None:
    print("Just right" if guess == guess_me else f"Too {'low' if guess < guess_me else 'high'}")

start = 1
count = 0

while count < 20:
    count += 1
    start += randint(-5, 5)
    guess_try(start)
    if start == guess_me:
        break

[print(i) for i in range(3,-1,-1)]
print({i for i in range(10) if i % 2})
pprint({i: i**2 for i in range(10)})
pprint({i for i in range(10) if not i % 2})


# ex 15 Counter
from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
b_counter = Counter(breakfast)
print(b_counter, b_counter.most_common(1))

launch = ['eggs', 'eggs', 'bacon']
l_counter = Counter(launch)
print(b_counter + l_counter)
print(b_counter - l_counter)
print(l_counter - b_counter)
print(l_counter & b_counter)
print(l_counter | b_counter)


# ex 16 Ordered Dict
from collections import OrderedDict

quote = OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk, nyuk!')])
for s in quote:
    print(s)


# ex 17 Deque
from collections import deque

def palindrome(word: str) -> bool:
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('hello'), palindrome('abba'))


# ex 18 chain, cycle, accumulate
from itertools import chain, cycle, accumulate

for item in chain([1, 2], ['a', 'b'], [[5, 6]]):
    print(item)

for item in cycle([1, 2]):
    print(item)
    if item == 2:
        break

for item in accumulate([1, 2, 3, 5, 9, 7], lambda x,y: x+2*y):
    print(item)


# ex 19
from zoo import hours as info
info()

plain = {'a': 1, 'b': 2, 'c': 3}
fancy = OrderedDict(plain)
print(plain, fancy)


# ex 20
class Duck:
    def __init__(self, input_name: str):
        self.__name = input_name
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, input_name: str) -> None:
        self.__name = input_name

quak = Duck('ducky')
print(quak.name)
quak.name = 'dooka'
print(quak.name)

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
    @property
    def diameter(self) -> int:
        return 2 * self.radius

circle = Circle(5)
print(circle.diameter)
circle.radius = 17
print(circle.diameter)


# ex 21
from collections import namedtuple
Duck = namedtuple('Duck', 'big tail')
duck = Duck('wild orange', 'crazy')
print(duck, duck.tail)
parts = {'big': 'cool', 'tail': 'not'}
duck2 = Duck(**parts)
print(duck2)
duck3 = duck2._replace(tail='toose')
print(duck3)


# ex 22
class Thing:
    pass

print(Thing)
example = Thing()
print(example)


# ex 23
import unicodedata

def unicode_test(value: str) -> None:
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value="{value}, name="{name}", value2="{value2}"')

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
print(unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE'))


# ex 24
from string import printable
import re
print(len(printable), printable)

for c in ['\d', '\w', '\s']:
    print(re.findall(c, printable))

x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w', x))

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''
print(re.findall('^I [wf]ish|fish tonight\.$', source))
print(re.findall('[wfsh]+ish', source))
print(re.findall(' m(?=ight)', source))


# ex 25

