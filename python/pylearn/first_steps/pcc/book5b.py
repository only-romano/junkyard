#! Занятие по книге Python Crash Course, chapter 5, "if statesments"
#! Занятие второе.

age = 27
if age >= 30:   # Simple "if" statement.
    print("Man, you're too old to break the rules and to haven't job at all")
    print("Stop bullshit man and finally get a job! God damn, man..")

# OMG, увидел тёлку из 1 серии стартрека в реальном обличье, страсть
# господня.  Звукоизоляция у них на корабле так себе.  У доктора
# Мак-Кой во второй серии такое кислое выражение :)  Ахах, все видят
# разных девушек.  Клёво.  Шеппард, это не от него ли Масс Эффектский
# Шеппард берёт своё имя ?)

else:   # Знаю что не по PEP-8, just for experiment :)
    print("You have to build your life in a few years, I swear")

if age < 4:      # Explain.  Ахахахах, Спок ржачный :)  И я не понял,
    print("You free to go") # почему кэп изменился, другой актёр?
    price = 0
elif age < 18:
    print("You've got to pay me $5 fee")
    price = 5
elif age <65:
    print("Admission cost for ya is $10")
    price = 10
else:       # Можно и без "else" обойтись крайним "elif'ом".
    price = 5

print("Your admission cost is $" + str(price) + ".")

# Ужастик прям вторая серия.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# Try it yourself 5-3.  Alien Colors №1.

alien_color = ['yellow', 'red', 'green']

for color in alien_color:   # Сосулька страшная во 2 серии.
    if color is 'green':
        print("Player just earned 5 point")

# Try it yourself 5-4.  Alien Colors №2:

for color in alien_color:
    if color is 'green':
        print("Player just earned 5 points for shooting the alien")
    else:
        print("Player just earned 10 points for shooting the alien")

# Try it yourself 5-5.  Alien Colors №3:

for color in alien_color:
    if color is 'green':
        print("Player just earned 5 points for shooting the alien")
    elif color is 'yellow':
        print("Player just earned 10 points for shooting the alien")
    elif color is 'red':
        print("Player just earned 15 points for shooting the alien")

# Try it yourself 5-6.  Srages of Life:

people = {"Mark": 11, "Eugene": 24, "Anna": 19, "Alice": 3,
          "Stuey": 1, "Granny": 78, "Sergio": 27}

for person in people:
    age = people.get(person)
    if age < 2:
        print(person.title(), "is a baby :)")
    elif age < 4:
        print(person.title(), "is a toddler ^^")
    elif age < 13:
        print(person.title(), "is a kid %)")
    elif age < 20:
        print(person.title(), "is a teenager @-@")
    elif age < 65:
        print(person.title(), "is a adult // !!")
    else:
        print(person.title(), "is a elder :^( ")

# Try it yourself 5-7.  Favorite Fruit:

fruits = ['pineapple', 'melon', 'orange', 'mango', 'apple', 'coconut',
          'strawberry', 'peach']

for fruit in fruits:
    if fruit in ['pineapple', 'orange', 'peach', 'watermelon']:
        print("You really like a " + fruit)
    elif fruit is 'coconut':
        print("It's not a fruit dumbass! It's a " + fruit)
    else:
        print(fruit.title(), "whatever..")

