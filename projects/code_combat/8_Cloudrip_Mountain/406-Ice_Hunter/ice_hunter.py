def isSubstring(word, substring):
    rightEdge = len(word) - len(substring) + 1
    for i in range(rightEdge):
        for j in range(len(substring)):
            shiftedIndex = i + j
            if word[shiftedIndex] != substring[j]:
                break
            if j == substring.length - 1:
                return True
    return False


enemies = hero.findEnemies()
for enemy in enemies:
    if isSubstring(enemy.id, "bos"):
        while enemy.health > 0:
            hero.attack(enemy)
