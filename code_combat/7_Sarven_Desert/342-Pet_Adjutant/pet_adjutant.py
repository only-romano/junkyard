def onHear(event):
    if event.message == "Fire":
        pet.moveXY(64, 16)
        pet.say("Meow fire!")
    elif event.message == "Heal":
        pet.moveXY(64, 52)
        pet.say("Meow help!")


pet.on("hear", onHear)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == "brawler":
            hero.say("Fire")
        else:
            hero.attack(enemy)
    else:
        if hero.health < hero.maxHealth / 2:
            hero.say("Heal")
