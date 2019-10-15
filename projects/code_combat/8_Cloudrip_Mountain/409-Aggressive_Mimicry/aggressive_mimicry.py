def startsWith(text, word):
    if len(word) > len(text):
        return False
    for i in range(len(word)):
        if word[i] != text[i]:
            return False
    return True


ogreNameStart = "Zog"

while True:
    suspectFriend = hero.findNearest(hero.findFriends())
    suspectName = suspectFriend.id
    if startsWith(suspectName, ogreNameStart):
        hero.attack(suspectFriend)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    else:
        hero.moveXY(27, 27)
