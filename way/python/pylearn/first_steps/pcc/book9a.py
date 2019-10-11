#! Занятие по книге Python Crash Course, chapter 9, "Classes".
# Занятие первое.

# Создание объекта из класса называется instantiation.  И работа идёт с
# instances класса.  Происходит указание информации, что хранится в
# инстансах и задаются действия, что будут выполнены с этими истансами.
# Можно думать о классах, как об инструкциях - как сделать инстанс.

# Также пишутся классы, расширяющие функциональность существующих
# классов, схожие классы могут делить код.

# The __init__() Method.

# Метод __init__() специальный, его Питон запускает автоматически когда
# создаётся новый инстанс, основанный на данном классе.  Параметр self
# необходимый элемент этого метода и должен идти первым среди
# параметров.  Каждое обращение к методу пропскает параметр self,
# который отсылает к собственно инстансу.  Каждая переменная с суффиксом
# self доступна любому методу в классе, а
# также к этим переменным есть доступ через любые инстансы, созданные из
# класса.
# Пример : "self.name = name" принимает значение, хранящиеся в параметре
# name и помещает значение в переменную name , которая после относится к
# инстансу, что был создан.  Переменные, которые доступны через инстансы
# называются атрибутами.

# МОЖЕШЬ ОБЪЯСНИТЬ ЧТО ТАКОЕ - ИНСТАНС?
from classes_book9 import Dog

my_dog = Dog('willie', 6)      # ЭТО ИНСТАНС?

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")

# А, понял.  Инстанс - это то, что возвращает __itit__() при
# инициализации класса строкой " my_dog = Dog(1, 2) " .

# По соглашению имена с большой буквы относят к классам в Python.
# Функция, которая является частью класса называется методом.  Инстансы,
# созданные из класса пишутся с маленькой буквы.  Доступ к атрибутам
# идёт через точку ( my_dog.name ) .

# Вызов методов из класса.
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)   # Ещё один инстанс.  Даже если использовать
# те же атрибуты - будет создан новый инстанс.  Можно создавать сколько
# угодно инстансов, каждый из которых должен иметь своё уникальное имя
# переменной или занимать уникальное место в листе или словаре.

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")
my_dog.sit()

print("\nYour dog's name is " + my_dog.name.title() + ".")
print("Your dog is " + str(my_dog.age) + "years old.")
your_dog.sit()

# Try it yourself 9-1, 9-2.  Restraunt.
from classes_book9 import Restaurant

restraunt1 = Restaurant('Бухич мухич', 'мулаточки')
restraunt1.describe_restraunt()
restraunt1.open_restraunt()

restraunt2 = Restaurant('Родина', 'патриоточки')
restraunt3 = Restaurant('Mon plesir', 'шлюшки')


restraunt2.describe_restraunt()
restraunt3.describe_restraunt()

from classes_book9 import User

user1 = User('serj', 'rome', '27', 'yes, please', 'python newbie')
user2 = User('anna', 'sys', '19', 'female', 'pedagogical')
user3 = User('jessie', 'angels', '18', 'female', 'economical')

user1.greet_user()
user1.describe_user()
user2.greet_user()
user2.describe_user()
user3.greet_user()
user3.describe_user()
