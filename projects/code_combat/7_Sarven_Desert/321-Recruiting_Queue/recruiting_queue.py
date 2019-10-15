neutrals = hero.findEnemies()
while True:
    if len(neutrals):
        hero.say(neutrals[0])
    else:
        hero.say("Nobody here")
    neutrals = hero.findEnemies()
