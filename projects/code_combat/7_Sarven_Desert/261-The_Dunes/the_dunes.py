while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type != "sand-yak" and enemy.type != "burl":
            distance = hero.distanceTo(enemy)
            if distance < 45:
                if distance <= 15 and hero.canCast("drain-life"):
                    hero.cast("drain-life", enemy)
                else
                    hero.attack(enemy)

    item = hero.findNearestItem()
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
    else:
        hero.moveXY(41, 31)
