# Модуль copy
from copy import copy, deepcopy


class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


harry = Animal("гиппогриф", 6, "розовый")
carrie = Animal("химера", 4, "зелёный горошек")
billy = Animal("богл", 0, "узорчатый")

my_animals = [harry, carrie, billy]

harriett = copy(harry)
print(harry.species, harriett.species)

more_animals = copy(my_animals)
print(more_animals[0].species)

# copy создаёт поверхностную копию
my_animals[0].species = "вампир"
print(my_animals[0].species, more_animals[0].species)

sally = Animal("сфинкс", 4, "песочный")
my_animals.append(sally)
print(len(my_animals), len(more_animals))

# deepcopy создаёт глубокую копию
new_animals = deepcopy(my_animals)
my_animals[0].species = "кися"
print(my_animals[0].species, new_animals[0].species)


# Модуль keyword
from keyword import iskeyword, kwlist

print(iskeyword('if'), iskeyword('ozwald'))
print(kwlist)


# Модуль random
from random import randint, choice, shuffle

# randint возвращает случайное число из заданного диапазона
print(randint(1, 100), randint(100, 1000), randint(1000, 5000))

num = randint(1, 100)

while True:
    guess = input("Угадайте число от 1 до 100! - ")
    try:
        guess = int(guess)
    except Exception:
        guess = 0

    if guess == num:
        print("Правильно!")
        break
    elif guess < num:
        print("Загаданное число больше!")
    elif guess > num:
        print("Загаданное число меньше!")


# choice возвращает случайный элемент списка
desserts = ['мороженое', 'блинчики', 'кекс', 'печенье', 'конфеты']
print(choice(desserts))


# shuffle перетасовывает элементы списка
print("До - %s" % desserts)
shuffle(desserts)
print("После shuffle - %s" % desserts)
