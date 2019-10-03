#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие третье.

user_0 = {
    'username': 'erermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():   # Метод возвращает ключ и значение.
    print('\nKey: ' + key)
    print('Value: ' + value)

for name in user_0.values():    # Ключи перебираются по умолчанию или
    print(name.title())         # Методом .keys() .

favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'phyton'
}

friends = ['phil', 'sarah']

for name in favorite_languages:
    if name in friends:
        print(" Hi! " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
    else:
        print(name.title() + " is a duchebag with it's " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, let's get some fuck tonite!")

a = 1
for name in sorted(favorite_languages.keys()):  # Сортировка библиотеки.
    a += 1
    print("Sorted assholes: ", a, "-", name)

# Перебор только уникальных значений.
for language in set(favorite_languages.values()):
    print(language.title())
