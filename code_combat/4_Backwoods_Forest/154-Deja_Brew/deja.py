potionsOnTheWall = 10
numToTakeDown = 1

while True:
    hero.say(potionsOnTheWall + " potions of health on the wall!")
    hero.say(potionsOnTheWall + " potions of health!")
    hero.say("Take " + numToTakeDown + " down, pass it around!")
    potionsOnTheWall -= numToTakeDown
    hero.say(potionsOnTheWall + " potions of health on the wall.")
