#! Книга "Python Crash Course", Глава 4. Working with Lists. Занятие 1.

magicians = ['alice', 'david', 'carolina']
for magucian in magicians:   # переменной присваивается значения списка
    print("To " + magucian.title() + ":\nThat was a great trick!")
    print("Can't wait to see Y next trick, " + magucian.title() + "!\n")

print("Thank you, everyone. That was a great magic show!\n")

letter = []
for number in range(1, 115**2, 7):      # побаловалась
    letter.append(-number**11)
print(letter)           # F[f[f[[ - угарная тема на заставке Star Trek )

# Офыбки: не причислить к циклу (ааааа, спок угарный :)) "Mister Spok
# here" f[f[f[f[]]]] ) ; логическая ошибка ; случайное определение к
# циклу или нециклу без надобности ; забывалкины двоеточий.

# PS: на каком смотреть?  Я английский знаю, но термины многие и тонкие
# веши могу не понять...  В общем, начала на английском, пока всё ясно.
# ахахаха, телефон у него ржачный :)  Точнее вызывалка.  Если я буду
# путешествовать в космосе - хочу чтобы там тоже было мартини :)  А
# капитан то влюбился. ОООО, планетка :)  A man, they're HUMANS ! ахаха
# Секси шмекси вышла, и большеголовые телик смотрят..

pizzas = ['peperoni', 'margarita', 'four seas']    # try-it-yourself 4.1
for pizza in pizzas:       # ЛОВУШКА!!!!! CAPTAIN !!!
    print(pizza)
    print("I fucking love " + pizza + "pizza!\n")
print("Oh, god, yes.. I incredibly love pizza.\n")    # Обезьяна вылезла

animals = ['pussycat', 'monkey', 'racoon']      # try-it-yourself 4.2
for animal in animals:
    print(animal.title())       # Красивый замок...  Хочу такой...
    print("A " + animal + " would make a great petting.\n")   # Мяф :)
print("Any of these animals would make a great petting!\n")

# Мочи его !!!  Captain vs. Barbarian.  Кинул кортик как боженька...

for value in range(1,5):    # Так пробел после запятой необязателен,
    print(value)            # а просто правило хорошего тона?

numbers = list(tange(1, 6))     # Прикольно, узнала как генерить лист..
print(numbers)      # А девушка-иллюзия то обиделась.  Это эти лунатики?

even_numbers = list(range(2, 11, 2))    # Even numbers = чётные числа
print(even_numbers)   # Так девушка иллюзия или реальная?  Не поняла.

squares = []        # Думала кэпа замочат...
for val in range(1, 11):    # По морде ему!  Ооо, он испугался.
    square = val ** 2
    squares.append(square)  # Они хотят чтобы он её трахнул или детей?
    # cooler = squares.append(val**2)   # Приколюха, я забыла про такое.
print(squares) # Они не могут читать мысли через примитивные эмоции.

# 2 вопроса - нужны пробелы после запятой или нет в range?  В последнем
# цикле - лучше читабельность или меньше строк?  Конец первого занятия.