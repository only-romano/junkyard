def isLetterInWord(searchWord, searchLetter):
    for i in range(len(searchWord)):
        if searchWord[i] == searchLetter:
            return True
    return False


engineer = hero.findFriends()[0]
safeLetter = engineer.safeLetter

enemies = hero.findEnemies()
for enemy in enemies:
    if isLetterInWord(enemy.id, safeLetter):
        while enemy.health > 0:
            hero.attack(enemy)
