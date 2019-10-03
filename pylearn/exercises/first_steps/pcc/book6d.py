#! Занятие по книге Python Crash Course, chapter 6, "Dictionaries".
# Занятие четвёртое.

# Try it yourself 6-4.

terms = {'dictionary': 'thery cool stuff to store data',
         'bug': 'shitty shit of whole shitness',
         'method': 'tools to do some tangs',
         'statement': 'something that is true or false',
         'variable': 'store cells to little data :)'}

terms['loop'], terms['value'] = 'cicle of poo', 'data'

for term, meaning in terms.items():
    print(term.title(), "is a", meaning)

# Try it yourself 6-5.

rivers = {'nile': 'egypt', 'ob': 'russia', 'sena': 'england'}

for river, country in rivers.items():
    print("River: ", river.title())
    print("Country: ", country.title())
    print("The " + river.title() + " runs through " + country.title() + ".")

# Try it yourself 6-6.

favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'
}

people = ['ben', 'sam', 'jen', 'kolya', 'edward', 'phil', 'serj', 'sarah']

p, c, r = 0, 0, 0
for man in people:
    if man in favorite_languages.keys():
        if favorite_languages[man] == 'python':
            p += 1
        elif favorite_languages[man] == 'ruby':
            r += 1
        elif favorite_languages[man] == 'c':
            c += 1
        print(man.title() + " votes for a " + favorite_languages[man] + '!')
    else:
        print(man.title() + ", man you are too dumb to vote.")

print("Voting results:\nPython: " + str(p) + "\nC: " + str(c) +
      "\nRuby: " + str(r))

