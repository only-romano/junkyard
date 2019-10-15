while True:
    horse = hero.findNearest(hero.findFriends())
    if horse:
        x1 = horse.pos.x - 7;
        x2 = horse.pos.x + 7;
        if x1 >= 1:
            hero.moveXY(x1, horse.pos.y)
        elif x2 <= 79:
            hero.moveXY(x2, horse.pos.y)

        distance = hero.distanceTo(horse)

        if distance <= 10:
            hero.say("Whoa")
            hero.moveXY(27, 54)
            hero.moveXY(42, 18)
