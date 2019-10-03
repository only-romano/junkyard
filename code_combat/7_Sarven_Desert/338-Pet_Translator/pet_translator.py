def onHear(event):
    message = event.message
    if message == "North":
        pet.say("Htron")
    if message == "South":
        pet.say("Htuos")
    if message == "East":
        pet.say("Tsae")


pet.on("hear", onHear);

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.type != "brawler":
        hero.attack(enemy)
