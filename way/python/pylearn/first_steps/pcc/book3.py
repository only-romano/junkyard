#!Книга "Python Crash Course", Глава 3. Introducing lists. Занятие 2.
#Продолжение работы со списками. Удаление элементов.
motorcycles = ['harley', 'bmw', 'kawasaki', 'yamaha']
print(motorcycles)
too_cool_for_me = 'yamaha'#хз  зачем было это делать, видимо исключительно, чтобы оправдаться за причину удаления. Ну, допустим.
motorcycles.remove(too_cool_for_me)#такой способ позволяет удалить элемент даже не зная индекс его. Естественно, можно и элемент напрямую, без переменных.
print(motorcycles)#С другой стороны, благодаря переменной - значение хранится в новой переменной и не потеряно окончательно.
print("\nA " + too_cool_for_me.title() + " is to cool for me.")#Способ remove() удаляет только первое повторение значения. Если лист содержит несколько - придётся циклировать.
persons = ['2pac', 'kurt cobain', 'napoleon', 'zhenya', 'serj tankian']#Задания.
for i in persons:
    print("Dear " + i.title() + ", I pleased to invite you to dinner next summer!")#try-it-yourself 3.4
    if i == "serj tankian":
        print("Regrets, " + i.title() + " can't make it.")#try-it-yourself 3.5
del persons[4]
persons.append('dostoyevsky')
for i in persons:
    print("My dear friend " + i.title() + ", I invite you to dinner next autumn, no discussions.")#try-it-yourself 3.5
print("Shiiiit. I gotta bigger table!")
persons.insert(0, 'schopengauwer')
persons.insert(2, 'mozart')
persons.append('babayka')
for i in persons:
    print("I swear, now it's final. My lovely " + i.title() + ", I have a wonderful plesure to invite you to my fancy dinner next winter!")#try-it-yourself 3.6
print("Holy fuck.")
print(persons)
for i in persons:
        persons.remove(i)
        print(i.title(), ", fuck off.")
for i in persons:
    if i == "zhenya":
        print("Сами покушаем.")
    else:
        persons.remove(i)
        print(i.title(), ", fuck off.")
print(persons)
person_rest1 = persons.pop(0)
print(persons)
person_rest2 = persons.pop()
print(persons)#try-it-youtself 3.7