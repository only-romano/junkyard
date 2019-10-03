def goToFlag(flag):
    hero.move(flag.pos)
    hero.pickUpFlag(flag)

def surviveYak(enemy):
    pos = hero.pos
    y = pos.y
    enY = enemy.pos.y
    if enY >= y:
        if hero.isPathClear(pos, {x: pos.x, y: y - 12}):
            y -= 12
        else:
            y += 12
    else:
        if hero.isPathClear(pos, {x: pos.x, y: y + 12}):
            y += 12
        else:
            y -= 12
    hero.moveXY(pos.x, y)


hero.moveXY(119, 31)

while True:
    flag = hero.findFlag()
    if flag:
        goToFlag(flag)

    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == "sand-yak":
        surviveYak(enemy)
        else:
            distance = hero.distanceTo(enemy);

            if distance < 30 and hero.canCast("chain-lightning"):
                hero.cast("chain-lightning", enemy)
            elif distance < 30 and distance > 10 and hero.canCast("poison-cloud"):
                hero.cast("poison-cloud", enemy)
            elif distance < 25 and hero.canCast("fear"):
                hero.cast("fear", enemy)
            elif distance < 15 and hero.health < hero.maxHealth and hero.canCast("drain-life"):
                hero.cast("drain-life", enemy)
            else:
                hero.attack(enemy)
