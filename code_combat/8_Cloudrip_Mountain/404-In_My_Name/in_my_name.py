def letterIndex(word, letter):
    for i in range(len(word)):
        character = word[i]
        if character == letter:
            return i
    return -1


ogreLetter = "z"
shaman = hero.findByType("thoktar")[0]

chestIndex = letterIndex(shaman.id, ogreLetter)
hero.moveXY(16 + chestIndex * 8, 36)
