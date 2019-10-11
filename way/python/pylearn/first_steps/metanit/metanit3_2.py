#! Работа с материалами Metanit, глава 3, часть 2. Кортежи.

user = ("Tom", 23)      # Кортеж является неизменяемым (immutable).
print(user)

user = "Tom", 23        # Кортеж можно записывать без скобок. Стоит ли?
print(user)

user = ("Tom",)         # Если один элемент у кортежа, записывать так.

users_list = ["Tom", "Bob", "Kate"]
users_tuple = tuple(users_list)
print(users_tuple)      # А так что будет? Будет users_list изменяться:
# users_list = users_tupple     Будет ли user_list способен измениться?
# users_tuple = users_list      А так останется ли кортеж неизменяемым?

print(users_tuple[0])       # Tom
print(users_tuple[2])       # Kate
print(users_tuple[-2])      # Bob

print(users_tuple[1:3])     # ("Bob", "Kate")

# users_tuple[1] = "Tom"      Такая запись работать не будет.

user = ("Tom", 22, False)       # Кортеж можно разобрать на отдельные
name, age, isMarried = user     # переменные.  Такая запись, присвоение
print(name, age, isMarried)     # несколько переменных - это круто!!!

def get_user():                 # Удобно использовать кортеж, когда надо
    name = "Tom"                # возвратить из функции сразу несколько
    age = 22                    # значений.  Когда функция возвращает
    isMarried = False           # их несколько - она возвращает кортеж.
    return name, age, isMarried

user = get_user()
print(user[0], user[1], user[2])    # Tom 22 False
print(len(user))                    # 3


# Перебор кортежей.

for item in user:           # Можно ли, чтобы он в одну строку print
    print(item)             # нескольких вещей делал в подобных кон-ях?

i = 0
while i < len(user):
    print(user[i])
    i += 1

name = "Tom"
if name in user:
    print("Пользователя зовут Tom")
else:
    print("Пользователь имеет другое имя")


# Сложные кортежи.

# Сразу вопрос, вроде из логики выходит так, но чисто удостовериться:
# если в кортеж засунуть списки или элементы - они же уже не смогут
# быть внутри кортежа изменены; собственно вопрос - есть ли разница,
# внести ли в кортеж как элемент другой кортеж или список - будет ли в
# этих случаях какая-то разница в функционале или каком-то наследовании
# уже внутри сложного кортежа?

countries = (               # Сложный кортеж, содержащий кортежи внутри.
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6))),
    ("Russia", 144.4, (("Moscow", 12.228), ("Omsk", 1.261))),
    ("Kazakhstan", 17.987, (("Astana", 1.014), ("Almaty", 1.713)))
)

for country in countries:
    countryName, countryPopulation, cities = country
    print("\nCountry: {}  population: {}".format(countryName, countryPopulation))
    for city in cities:
        citiName, citiPopulation = city
        print("City: {}  population: {}".format(citiName, citiPopulation))

# Офигенные две штуки понял.  Про скобочки {} - как их можно пользовать,
# если бы подумал раньше над функциями проверки задачек - то можно было
# бы понять..  Но тут прям очевидно.  В общем, я понял.  Ну и вторая
# крутая штука - это ".format", тоже крутая штука.  Надо разобраться.
