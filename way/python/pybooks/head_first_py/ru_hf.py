# diy 1
from datetime import datetime

odds = (i for i in range(1, 60, 2))
this_minute = datetime.today().minute

print("This minute seems a little odd." if this_minute in odds else "Not an odd minute.")


# diy 2
from os import getcwd
print(getcwd())


# diy 3
import time
from random import randint

today = time.strftime("%A")

if today == 'Saturday':
    print('Party!!')
elif today == 'Sunday':
    print('Recover.' if randint(1, 5) > 2 else 'Rest.')
else:
    print('Work, work, work.')


# diy 4
word = "bottles"
for beer_num in range(99, 0, -1):
    bn = f'{beer_num} {word}'
    print(f'{bn} of beer on the wall.\n{bn} of beer.\nTake one down. Pass it around.')
    if beer_num == 1:
        print(f"No more {word}s of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(f'{new_num} {word} of beer on the wall')
    print()


# diy 5
vowels = set('aeiou')
word = 'Hava Nagila' # and input('Provide a word to search for vowels: ')
found = set()

for letter in word:
    letter = letter.lower()
    if letter in vowels:
        found.update(letter)

for vowel in found:
    print(vowel)


# diy 6
nums = [1, 2, 3, 99, 4]
nums.remove(99)
print(nums)
nums.extend([5, 6])
print(nums)
nums.insert(0, 0)
print(nums)
nums.insert(3, "two-and-a-half")
print(nums)


# idy 7
book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
backwards = book[::-1]
print(backwards)
every_other = ''.join(booklist[::2])
print(every_other)


# idy 8
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = "".join(plist[1:3] + plist[5:3:-1] + plist[7:5:-1])
print(new_phrase)


# diy 9
paranoid_android = "Marvin, the Paranoid Android"
for char in paranoid_android[:6]:
    print(f"\t{char}")
for char in paranoid_android[-7:]:
    print(f"\t\t{char}")
for char in paranoid_android[12:20]:
    print(f"\t\t\t{char}")


# diy 10
persona9 = {
    'Name': 'Ford Prefect',
    'Gender': 'Male',
    'Occupation': 'Researcher',
    'Home Planet': 'Betelgeuse Seven',
}

print(persona9['Home Planet'])
persona9['Age'] = 33


# diy 11
word = 'Hanted Inversal You\'ll be thery happy man!' #and input("Input word: ")
word_vowels = {v:0 for v in vowels}
for letter in word:
    low = letter.lower()
    if low in vowels:
        word_vowels[low] += 1

print(word_vowels)

for k, v in sorted(word_vowels.items()):
    print(f'{k} was found {v} time{"" if v == 1 else "s"}')


# diy 12
lists = (["a", "b", "c"], {1,2,3}, (5,6,7))
lists[0].append("d")
lists[1].update([5,3,2])
lists[1].add(4)
print(lists)


# diy 13
data = (
    ("Форд Префект", "Мужской", "Исследователь", "Бетельгейзе 7"),
    ("Артур Дент", "Мужской", "Приготовление бутербродов", "Земля"),
    ("Гриша МакМиллан", "Женский", "Математик", "Земля"),
    ("Марвин", "Неизвестен", "Робот-параноик", "Неизвестна")
)

heroes = {}

for el in data:
    heroes[f'persona{len(heroes)+1}'] = {
        "Name": el[0], "Gender": el[1], "Occupation": el[2], "Home World": el[3]
    }
print(heroes)


# diy 14
from pprint import pprint

names = ["Ford", "Arthur", "Trillion", "Robot"]
for i in range(4):
    key = f"persona{i+1}"
    heroes[names[i]] = heroes[key]
    del heroes[key]

pprint(heroes)
pprint(heroes['Arthur']['Occupation'])


# diy 15
def search4letters(have:bool=True, letters:set=()) -> set:
    vowels = letters if letters else set('aeiou')
    word = input("Provide a word to search for vowels: ")
    if have: found = vowels.intersection(set(word))
    else:    found = set(word).difference(vowels)
    for vowel in found:
        print(vowel)
    return found
# search4letters()
# search4letters(vowel=False)
# search4letters(letters=("a", "b", "c", "d", "e"))


# diy 16
def search_intersection(phrase:str="", letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase if phrase else input("Input phrase")))

print(search_intersection("hello", 'alalaol'))


# diy 17
import vsearch
print(vsearch.search4letters("whello", "el"))


# diy 18
def double(arg):
    print(f'Before: {arg}')
    arg = arg * 2
    print(f'After: {arg}')

def change(arg):
    print(f'Before: {arg}')
    arg.append('More data')
    print(f'After:  {arg}')

num = 10
double(num)
print(num)
saying = 'Hello '
double(saying)
print(saying)
numbers = [42, 256, 16]
double(numbers)
print(numbers)

change(numbers)
print(numbers)
