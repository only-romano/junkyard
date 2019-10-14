# sys - управление интерпретатором Python
from sys import exit, stdin, stdout, version

# выход из оболочки или консоли Python
# exit()

# stdin.readline - пользовательский ввод с возможностью ограничения количества символов
v = "1234"  #stdin.readline(4)

# stdout.write - вывод в консоль с подсчётом символов
stdout.write(v)

# version - информация о версии Python
print(version)


# time - модуль работы со временем
import time

# time.time - функция возвращает секунды с полуночи 1 января 1970
print(time.time())

def slowfunc(num):
    n = 0
    for i in range(num):
        for j in range(num):
            n += j
    return n

t1 = time.time()
num = slowfunc(1000)
t2 = time.time()
print("Число - %s, прошло времени - %s" % (num, t2 - t1))

# asctime - перевод кортежа в человеческую дату
print(time.asctime())
t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))

# localtime - возвращает объект с текущей датой
t = time.localtime()
print(t, t[0], t[1])

# sleep - пауза в выполнении программы
for x in range(1, 6):
    print(x)
    time.sleep(0.5)


# pickle - модуль для преобразования информации в удобный для записи в файл формат
import pickle

game_data = {
    "позиция": 'C23 B45',
    "карманы": ['ключи', 'карманный нож', 'гладкий камень'],
    "рюкзак": ['веревка', 'молоток', 'яблоко'],
    "деньги": 158.50
}

save_file = open('save.dat', 'wb')
pickle.dump(game_data, save_file)
save_file.close()

load_file = open('save.dat', 'rb')
loaded_game_data = pickle.load(load_file)
load_file.close()

print(loaded_game_data)


# Упражнение 1. Копирование
import copy

class Car:
    pass

car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)  # 3

car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)  # 3


# Упражнение 2. Запись и загрузка

favorites = ["ничего", "нет", "я", "один"]
file_fav = open("favorites.dat", 'wb')
pickle.dump(favorites, file_fav)
file_fav.close()

file_fav_open = open("favorites.dat", 'rb')
loaded_fav = pickle.load(file_fav_open)
file_fav_open.close()

print(loaded_fav)
