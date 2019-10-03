
def equals(string):
    mass, lib = string.split(' '), {}
    while mass:
        word = mass.pop()
        for a in word:
            try:
                if int(a) in range(1, 10):
                    lib[a] = word
            except:
                pass
    for key, word in sorted(lib.items()):
        mass.append(word)
    return ' '.join(mass)


print(equals("is2 This1 tes4t 3a"))
print(equals(''))
