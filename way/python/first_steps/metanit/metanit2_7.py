#!Учебный код по программе Метанит, Глава 2, часть 7. Циклы. Занятие 1.
#Цикл While.
choice = input("y/n: ")
while choice.lower() == "y":
	print ("Привет")
	choice = input("Для продолжения нажмите \"y\", а для выхода любую другую клавишу: ")
print("Работа программы завершена\n")#Каждый проход цикла называется итерацией. Циклы выполняются пока условия соответствуют true.

#! Программа по вычислению факториала. Копяи в factorial.py.
number = int(input("Введите число: "))
i = 1
factorial = 1
while i <= number:
	factorial *= i
	i += 1#Пока счётчик i не превысит числа, будет выполняться цикл.
print("Факториал числа", number, "равен", factorial)

#Цикл For. Формат - for переменная, хранящая целые числа in функтция range(): \n\tинструкции
#! Программа по вычислению факториала, версия 2. Копяи в factorial.py.
number = int(input("Введите число: "))
factorial = 1
for i in range(1, number+1):#При выполнении цикла числа создаваемые range сохраняются в переменной.
	factorial *= i#При первом проходе цикл получает первое число, при втором - второе и тд, пока не переберёт все. Тогда цикл завершает работу.
print("Факториал числа", number, "равен", factorial)#Циклы выполняются ДО крайнего аргумента range, не включительно.

#Функция Range. Формы - range(stop): возвращает все целые числа от 0 до stop (не включая);
#range(start, stop): возвращает все целые числа от start(включая) до stop(не включая);
#range(start, stop, step): возвращает все целые числа от start(включая) до stop(не включая), увеличивающиеся на значение step. Примеры:

print("\n\n","Примеры функции Range():")

print("\n\n",range(5), ":")
for i in range(5):
	print("\t", i, end=" ")

print("\n\n",range(1, 5), ":")
for i in range(1, 5):
	print("\t", i, end=" ")

print("\n\n",range(2, 10, 2), ":")
for i in range(2, 10, 2):
	print("\t", i, end=" ")

print("\n\n", range(5, 0, -1), ":")
for i in range(5, 0, -1):
	print("\t", i, end=" ")

#Вложенные циклы.
print("\n\n\n", "Табличка умножения:\n")
for i in range(1,10):#Табличка умножения. Внешний цикл срабатывает 9 раз.
	for j in  range(1,10):#Внутренний цикл срабатывает 9 раз для каждой интерации (срабатывания) внешнего цикла.
		print(i*j, end="\t")#В каждой интерации будет выводиться произведение i и j.
	print("\n")
print("\n\n\tКонец :)")
#Конец занятия.