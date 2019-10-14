#! Занятие по книге Python Crash Course, chapter 8, "Functions".
# Занятие третье.


def greet_users(names):
    """A simple greeting to each user in the list."""
    for name in names:
        print("Hello, " + name.title() + "!")


greet_users(['hannah', 'ty', 'margot'])


def print_models(unprinted_designs, completed_models=[]):
    """Simulates printing design until none are left"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(['iphone case', 'robot pendant', 'dodecahedron'])

# Использование копии данных для оставления первоночального источника
# неизменным.  [:] - делает копию листа.
list_models = ['1 item', '2 item', '3 item']
print_models(list_models[:])

print_models(list_models)

magicians = ['albert', 'gudinni', 'blane']


def show_magicians(magicians):
    """Try it yourself 8-9, 8-10"""
    temp = []
    while magicians:
        magician = magicians.pop()
        print(magician.title())
        magician = "Great " + magician.title()
        temp.append(magician)
    magicians = temp
    print(magicians)


show_magicians(magicians[:])        # Try it yourself 8-11.
print(magicians)


# Passing an arbitary number of arguments.
# Имя параметра со звёздочкой обозначает, что питон создаст кортеж под
# именем параметра и запакует туда все переданные аргументы.  Имя
# параметра типа arbitary стоит последним.


def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    """
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'mushrooms', 'green peppers', 'extra cheese')


# Использование неопределённых наборных аргументов. ** - Питон создаёт
# пустую библиотеку и пакует связки "ключ-значение".


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first name'], profile['last name'] = first, last
    for key, value in user_info.items():
        profile[key] = value
    return profile


print(build_profile('albert', 'einstein', location='princeton',
                    field='physics'))


def make_sandwich(*pieces):
    """Try it youtself 8-12."""
    print("\nMaking sandwich with:")
    for piece in pieces:
        print("- " + piece)


make_sandwich('cheese', 'ham', 'pepper')
make_sandwich('tune', 'soup cream')
make_sandwich('peanut butter')


# Tty it yourself 8-13.
print(build_profile('serj', 'diforverri', location='omsk',
                    field='programming', sex='arbitary'))


def make_car(manufacturer, model, **car_info):
    cars = {}
    cars['manufacturer'], cars['model'] = manufacturer, model
    for key, value in car_info.items():
        cars[key] = value
    return cars


print(make_car('mazda', 'millenia', color='white', speed="220"))
