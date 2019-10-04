#!Работа с книгой Python Crash Course, глава 3, занятие 3.
#Сортировка и управление листом.
cars = ['mazda', 'lotus', 'gmc', 'caddilac']
cars.sort()#сортировка по алфавиту, если все элементы представленны в одном виде (без заглавных или наоборот), иначе соответственно привести к единому формату методами.
print(cars)#такая сортировка изменяет порядок листа на постоянной основе.
cars.sort(reverse=True)#аргумент реверс, для обратоной сортировки.
print(cars)

print("\nsorted:\n" + str(sorted(cars)))#временная сортировка, для того чтобы посмотреть, порядок самого списка не изменяется. Функция sorted() может принимать аргумент reverse.

#Сортировка в разном виде форматов. Сама захотела сделать.
hoods = ['englewood', 'Compton', 'Hills']
print(hoods)
z=-1
for i in hoods:
    hoods.remove(i)
    def func(i):
        x=str(i.lower())
        return x
    i = func(i)
    z+=1
    z=int(z)
    hoods.insert(z, i)
hoods.sort()
print(hoods)
hoods = ['englewood', 'Compton', 'Hills']
print(hoods)
z=-1
for i in hoods:#оптимизировала изначальный бешщеный и лишний хаос. То оставила чтобы ты понял, как я рассуждала.
    hoods.remove(i)
    z+=1
    hoods.insert(z, str(i.lower()))
print(sorted(hoods))
#Не знаю, зачем запарилась - этого не было в заданиях, просто самой интересно было сделать. И сделала :) Как смогла. Но! Сортирует и лоуэр и аппер кейс :)

cars=['mazda', 'lotus', 'gmc', 'caddilac']
cars.reverse()#реверс без упорядовачивания.
print(cars)#кстати не заработала команда print(cars.reverse()) - выдала None. Подозреваю, что тут cars.reverse() не значение, а операция или как-то так.
print(len(cars))#выдаёт длинну списка, отсчёт ведётся с 1, а не с 0. то есть 4 элемента = 4, а не 3.

places = ['tokyo', 'bali', 'antarctida', 'miami', 'los angeles']#try-it-yourself 3.8
print(str(places) + "\n" + str(sorted(places)))
print(str(places) + "\n" + str(sorted(places, reverse=True)))#провозилась с реверсом, подбирала как тут аргумент ставить...
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
print("There are " + str(len(hoods)) + " hoods.")#try-it-yourself 3.9
#try-it-yourself 3.10 Отдельным файлом book3b_tiy310.py