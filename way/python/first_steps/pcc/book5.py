#! Занятие по книге Python Crash Course, chapter 5, "if statesments"
#! Занятие первое.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':        # False или True, выдаваемое конструкцией,
        print(car.upper())  # называется - conditional test - тест на
    else:                   # состояние.  Эквивалент: == простейший тест
        print(car.title())  # на состояние.  Не путать с присвоением: =.

car = 'Audi'    # ЕСТЬ РАЗНИЦА МЕЖДУ ОДИНОЧНЫМИ И ДВОЙНЫМИ КАВЫЧКАМИ ?

if car.lower() == 'audi':   # Тесты на состояние не изменяют переменную.
    print(car)

topping = ['mushrooms', 'extra-cheese', 'grilled bacon', 'pineapple']

for requested_topping in topping:   # просто повтарение - мать учения,
    if requested_topping != 'anchovies':    # перебдю, чем недобдю.
        print("Hold the anchovies!")
        break       # Чтобы не захламлять запускалку.

# Кстати, уже можно тестики писать, где if'ами будет проверяться
# правильность ответа (копия в podkat_k_programmistke.py):

print("Привет, красотка, гоу метафазиться!")
answer = str(input("Ну, что скажешь ?): "))

if answer.lower() in ("yes афк пошли мяф го игого"
        "гоу хочу молодец красава мечтаю давай ага супер пойдём"):
    print("Ah Eh, let's go baby!")
else:
    right_answer = str(""
                       "")
    while answer.lower() not in ("yes афк пошли мяф го игого"
        "гоу хочу молодец красава мечтаю давай ага супер пойдём"):
        print("Некорректный ответ, пожалуйста, повторите попытку")
        answer = str(input("Ещё попыточка: "))
    print("Finally. Why does it took so long?")

age1, age2 = [21, 22]  # Как я люблю присвоение нескольких переменных...
# Решил сделать рукодельное "исключительное ИЛИ":
print((age1 >=21 or age2 >= 21) and (age1 < 21 or age2 < 21))

# Boolean values - True \ False.

# Try it yourself 5-1 (daily routine... just for LOLs):
car = ['mazda', 'millenia']
cars = ['shit', 'lincoln navigator', 'mazda xedos 3', 'porshe cayene',
        'mazda rx-8', 'bugatti b110', 'ferrari f50', 'mercedes s55amg',
        'mazda millenia', 'girlfriend']

for model in cars:
    print("What kind of car you've got?")
    if car[0] in model:
        print("Oh, Mazda, cool! Is it Millenia?")
        if car[1] in model:
            print(model.title() + "!!! Fucking AWESOME !!!\n")
        else:
            print("Whatever, " + model.title() + " it's cool too.\n")
    else:
        print(model.title() + "? Shit happens.\n")

# Try it yourself 5-2.  OMG, it's too boooooooriiiiiing :(((
bella, donna, cat, sex = ['pregnant', 'not pregnant', 'Rhyzulka', 'cool']
tuple_muple = ('cool', 'pregnant', 'sex')
print((bella == 'not pregnant'), (donna == 'not pregnant'),
      (cat == 'rhyzulka'), (cat.lower() == 'rhyzulka'),
      (0 >= 1), (11 == 2 + 9), (6 != 3*2), (2*2 > 3), (3 < 2),
      (23 <= 11**2), (sex == 'cool' and bella == 'pregnant'),
      (sex != 'cool' or bella == 'not pregnant'), (sex in tuple_muple),
      (bella not in tuple_muple))


#! Занятие второе.
