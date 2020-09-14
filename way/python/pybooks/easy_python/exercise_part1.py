from pprint import pprint

# ex 1
seconds_per_hour = 60*60
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day/seconds_per_hour == seconds_per_day//seconds_per_hour)


# ex 2
s1 = { 1, 2, 3, 4, 5, 6 }
se = { 0, 2, 4, 6, 8 } 
so = { 1, 3, 5, 7, 9 }

print(s1 & so)
print(s1 | so)
print(s1 ^ so)
print(s1 >= so, s1 <= so, s1 > so, s1 < so)
print(s1|so >= so, s1 <= se|so)


# ex 3
years_list = range(1990, 1996)
third_bday = years_list[3]
print(third_bday)
print(max(years_list))

things = ['mozzarella', 'cinderella', 'salmonella']
print(things[1].capitalize(), things)
print(things[0].upper(), things)
things.remove('salmonella')
print(things)

surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise[-1].lower())
print(surprise[-1][::-1].lower().capitalize())


# ex 4
en2fr = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse",
}

print(en2fr["walrus"])

fr2en = {v: k for k, v in en2fr.items()}
print(fr2en["chien"])
print(set(en2fr))


life = {
    'animals': {
        'cats': [ "Henri", "Grumpy", "Lucy" ],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}
print(*life.keys())
print(*life['animals'].keys())
print(*life['animals']['cats'])


# ex 5
