workerNameList = hero.findNearest(hero.findFriends()).workerList


def build(construction, start):
    for i in range(start, workerNameList.length, 3):
        hero.say(workerNameList[i] + " - " + construction)


build("tower", 1)
build("tent", 0)
build("fence", 2)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
