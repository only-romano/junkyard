spell = "VENI"
wizard = hero.findNearest(hero.findFriends())
powerMap = wizard.powerMap


def convert(row, col):
    return {"x": 16 + col * 12, "y": 16 + row * 12}


for i in range(len(powerMap)):
    for j in range(len(powerMap[i])):
        point = powerMap[i][j]
        if point > 0:
            pos = convert(i, j)
            hero.moveXY(pos["x"], pos["y"])
            hero.say("VENI")
            enemy = hero.findNearestEnemy()
            if enemy:
                if hero.canCast("regen"):
                    hero.cast("regen", hero)
                if hero.canCast("shrink"):
                    hero.cast("shrink", enemy)
                while enemy.health > 0:
                    hero.attack(enemy)
            item = hero.findNearestItem()
            if item:
                hero.moveXY(item.pos.x, item.pos.y)
