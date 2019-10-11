#! Занятие по книге Python Crash Course, chapter 8, "Functions".
# Занятие первое.


def greet_user(username):               # username - параметр функции.
    """Display a simple greeting."""    # Документация функции.
    print("Hello, " + username.title() + "!")


greet_user('jesse')                     # jesse - аргумент функции.

# Try it yourself 8-1, 8-2.


def display_message(name, book):
    print('Hey, ' + name.title() + "! I'm learning about functions. The '" +
          book.title() + "' is also my favorite book.")


display_message('sergio', 'demons')


# Passing arguments.  Параметров функции может быть множество


def describe_pet(pet_name, animal_type='dog'):
    """Display informftion about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# Positional arguments.  Аргументы по позиции.
describe_pet('harry', 'hamster')
describe_pet('willie')

# Значение порядка аргументов функции.
describe_pet('hamster', 'harry')   # У меня есть гарри, его зовут Хомяк.

# Keyword arguments.  Аргументы по ключевому слову напрямую.
describe_pet(animal_type='cat', pet_name='rhyzik')
describe_pet(pet_name='lisa')

# Default values.  Параметры со значениями по умолчанию должны
# находиться после неустановленных по умолчанию параметров.  Так должно
# быть из-за позиционного расположения аргументов.
describe_pet(pet_name='willie')

# Errors.
# describe_pet()

# Try it yourself 8-3, 8-4.  Wet T-shirts.


def make_shirt(message='I love Python', size='wet'):
    print("Here's your " + size + " shirt with a message: '" +
          message + "' on it!")


make_shirt('Poop', 'small')
make_shirt(size='medium', message='Hegel Rules!')
make_shirt()
make_shirt(size='medium')
make_shirt(message='Sexy')

# Try it yourself 8-5.  Cities.


def describe_city(city, country='russia'):
    print(city.title() + " is in " + country.title() + ".")


describe_city('omsk')
describe_city(city='moscow', country='russia')
describe_city('almaty', 'kazakhstan')
