#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие шестое.

# Лист как значение словаря.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, langueges in favorite_languages.items():
    if len(langueges) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for languege in langueges:
            print("\t" + languege.title())
    else:
        for languege in langueges:
            print("\n" + name.title() + "'s favorite language is:\n"
                  "\t" + languege.title())

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# Try it yourself 6-7.


person = {
    0: {'name': 'Mike', 'surname': 'Dick', 'city': 'Los Angeles'},
    1: {'name': 'John', 'surname': 'Leonard', 'city': 'London'},
    2: {'name': 'Alice', 'surname': 'La Bouche', 'city': 'Paris'},
    3: {'name': 'Ruslan', 'surname': 'Bobrow', 'city': 'Kazan'},
    4: {'name': 'Xing', 'surname': 'Chung', 'city': 'Beijing'},
}

person[5] = {'name': 'Maria', 'surname': 'Smuglanka', 'city': 'Kiev'}
person[6] = {'name': 'Abu', 'surname': 'Makabu', 'city': 'Capablanca'}

for people in person:
    print("This is " + person[people]['name'] + " " + person[people]['surname'] +
          " from " + person[people]['city'] + ".")
