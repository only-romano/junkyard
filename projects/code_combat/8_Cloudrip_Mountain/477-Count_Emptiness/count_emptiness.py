def moveNSteps(n):
    hero.moveXY(hero.pos.x + 8 * n, hero.pos.y)


riddle = hero.findNearestEnemy().riddle
trimmed = riddle.strip()
moveNSteps(len(riddle) - len(trimmed))
hero.say("Gotcha!")
