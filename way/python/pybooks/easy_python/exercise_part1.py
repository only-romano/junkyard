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
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes) 
the_byte_array = bytearray(range(0, 256))
print(the_byte_array)

import struct
print(struct.pack('>L', 154))

import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
print(binascii.unhexlify(b'89504e470d0a1a0a'))

a = 0b1001
b = 0b0011
print(a & b, a | b, a ^ b, ~a, a << 1, a >> 1)


# ex 26
mystery = '\U0001f4a9'
print(mystery, unicodedata.name(mystery))

pop_bytes = bytes(mystery.encode('utf-8'))
print(pop_bytes)
pop_string = pop_bytes.decode('utf-8')
print(pop_string)

print('''My kitty cat likes %s
My kitty cat likes %s
My kitty cat fell on his %s
And now thinks he's a %s''' % ('roast beef', 'ham', 'head', 'clam'))

response = {
    'salutation': 'howdy-how',
    'name': 'Romeo',
    'product': 'love potion',
    'verbed': 'spoiled the show',
    'room': 'gym-class',
    'animals': 'peacock',
    'amount': '5 pounds',
    'percent': '93',
    'spokesman': 'Doggy Dog',
    'job_title': 'Mayor of California'
}

letter = '''Dear {salutation} {name}.
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}'''.format(**response)
print(letter)

mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon
'''

print(re.findall(r'\bc[\w]*', mammoth))
print(re.findall(r'\bc[\w]{3}\b', mammoth))
print(re.findall(r'\br[\w]*', mammoth))
print(re.findall(r'\b[\w]*[aeiou]{3}[\w]*\b', mammoth))

gif = binascii.unhexlify('4749463839610100010080000000000ffffff21f9' + 
    '0401000000002c00000000100010000020144003b')
print(gif, binascii.hexlify(gif[6:8]), binascii.hexlify(gif[8:10]))


# ex 27
import csv

villians = (
    ('Doctor', 'No'),
    ('Rosa', 'Klebb'),
    ('Mister', 'Big'),
    ('Auric', 'Goldfinger'),
    ('Ernst', 'Blofeld')
)

with open('villians.csv', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villians)

with open('villians.csv', 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]

with open('villians.csv', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    dic_villains = [row for row in cin]

print(villains, villians)
pprint(dic_villains)


# ex 28
import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
list_dict = {}
print(root.tag)
for child in root:
    print(child.tag, ": ", child.attrib)
    list_dict[child.tag] = child.attrib
    for gradndchild in child:
        list_dict[child.tag].update({gradndchild.text: gradndchild.attrib})
        print(f'\t{gradndchild.tag}: {gradndchild.attrib}')


# ex 29
import json
from datetime import datetime

menu_json = json.dumps(list_dict)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

now = datetime.utcnow()
print(now)

json.dumps(str(now))


# ex 30
import dbm
db = dbm.open('definitions', 'c')
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'
print(len(db), db['pesto'])
db.close()


# ex 31
test1 = 'This is a test of the emergency text system'
with open('test.txt', 'w') as file:
    file.write(test1)

with open('test.txt', 'r') as file:
    test2 = file.read()
    print(test1 == test2)


# ex 32
import os

fout = open('oops.txt', 'wt')
print('Oops, I created a file', file=fout)
fout.close()

print(os.path.exists('oops.txt'), os.path.exists('./oops.txt'))
name = 'oops.txt'
print(os.path.isfile(name), os.path.isdir(name), os.path.isdir('.'))
print(os.path.isabs(name), os.path.isabs('/big/fake/name'))

import shutil

shutil.copy('oops.txt', 'ohno.txt')
shutil.move('ohno.txt', 'ohyes.txt')
os.rename("ohyes.txt", 'ohwell.txt')
os.link('oops.txt', 'yikes.txt')
# os.symlink('oops.txt', 'jeepers.txt')  - can't do on windows
