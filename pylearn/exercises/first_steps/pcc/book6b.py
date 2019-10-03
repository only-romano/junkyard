#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие второе.

alien_0 = {'color': 'green', 'points': 5}

del alien_0['points']   # Убаляет пару ключ-значение навсегда.
print(alien_0)

favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'phyton'
}

# Try it yourself 6-1, 6-2, 6-3:

person = {
    0: {'nmae': 'Mike', 'surname': 'Dick', 'city': 'Los Angeles'},
    1: {'name': 'John', 'surname': 'Leonard', 'city': 'London'},
    2: {'name': 'Alice', 'surname': 'La Bouche', 'city': 'Paris'},
    3: {'name': 'Ruslan', 'surname': 'Bobrow', 'city': 'Kazan'},
    4: {'name': 'Xing', 'surbame': 'Chung', 'city': 'Beijing'}
}

person[0]['number'], person[1]['number'], person[2]['number'] = 13, 17, 11
person[3]['number'], person[4]['number'] = 101, 'p'

person[0]['know'] = {'dictionary': 'thery cool stuff to store data'}
person[1]['know'] = {'bug': 'shitty shit of whole shitness'}
person[2]['know'] = {'method': 'tools to do some tangs'}
person[3]['know'] = {'statement': 'something that is true or false'}
person[4]['know'] = {'variable': 'store cells to little data :)'}

for people in person:
    print('\n')
    for man in person[people]:
        print(person[people][man])
