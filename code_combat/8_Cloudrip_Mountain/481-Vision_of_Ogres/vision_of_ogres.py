def findRealEnemy(enemies):
    for enemy in enemies:
        name = enemy.id.lower()
        words = name.split(" ")
        second = words[1]
        if second[0] == second[-1]:
            return enemy


while True:
    ogres = hero.findEnemies()
    realOgre = findRealEnemy(ogres)
    if realOgre:
        while realOgre.health > 0:
            hero.attack(realOgre)
