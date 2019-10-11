#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие седьмое.

# Try it yourself 6-8.

rhyzhik = {'cat': 'sergio'}
bobik = {'dog': 'irina'}
liza = {'dog': 'eugenious'}

pets = [rhyzhik, bobik, liza]

for pet in pets:
    for k, v in pet.items():
        print(v.title() + " has a " + k + '.')


# Try it yourself 6-9.

favorite_places = {'Angeline': ['Los Angeles', 'New York', 'Honolulu'],
                   'Jessica': ['Tokyo', 'Barcelona', 'Rio-De-Janeiro'],
                   'Sergio': ['Angeline', 'Miami', 'Jessica'],
                   }

for man in favorite_places:
    print("\nHey, " + man + ", what is your favorite places?")
    print("My favorite places are: " + favorite_places[man][0] + ", " +
          favorite_places[man][1] + ", " + favorite_places[man][2] + ".")


# Try it yourself 6-10.

persons = {'Serj': 17, 'Lisa': 11, 'Alice': 13, 'Sam': 111}

persons['Lisa'] = [11, 7]
persons['Sam'] = [111, 22]
print("\n")

for person in persons:
    if isinstance(persons[person], list):
        print(person.title() + "'s favorite numbers are " + str(persons[person][0]) +
          ", " + str(persons[person][1]) + '.')
    else:
        print(person.title() + "'s favorite number is " + str(persons[person]) +
          '.')


# Try it yourself 6-11.

cities = {'Miami': {'info': 'city of my dream', 'country': 'USA',
                    'population': '5.56 mln', 'fact': 'major port of atlantic'},
          'Omsk': {'info': 'city of my now-a-days reality', 'country': 'Russia',
                   'population': '1.25 mln', 'fact': 'my hometown'},
          'Paris': {'info': 'qua-qua', 'country': 'France qua',
                    'population': '~6 mln', 'fact': 'too qua for me'}
}

for city in cities:
    print("The " + city + " is a " + cities[city]['info'] + ". " +
          cities[city]['country'] + ". Population of the city is " +
          cities[city]['population'] + ". And all I know about it is that " +
          city + " is " + cities[city]['fact'] + ".")

print("\n")


# Try it yourself 6-12.

hz_info, hz_country, hz_pop, hz_fact = 'for real hz', 'HZ', 'hz bln.', 'hz'
cities['Hz'] = {}
cities['Hz']['info'] = hz_info
cities['Hz']['country'] = hz_country
cities['Hz']['population'] = hz_pop
cities['Hz']['fact'] = hz_fact

for city in cities:
    print("The " + city + " is a " + cities[city]['info'] + ". " +
          cities[city]['country'] + ". Population of the city is " +
          cities[city]['population'] + ". And all I know about it is that " +
          city + " is " + cities[city]['fact'] + ".")
