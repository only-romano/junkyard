def getKey(name):
    key = pet.findNearestByType(name)
    if key:
        pet.fetch(key)

def onSpawn(event):
    getKey("bronze-key")
    getKey("silver-key")
    getKey("gold-key")


pet.on("spawn", onSpawn)

while True:
    enemy = hero.findNearestEnemy()
    if enemy and enemy.team == "ogres":
        hero.attack(enemy)
    
    if hero.health < 300:
        potion = pet.findNearestByType("potion")
        if potion:
            hero.moveXY(potion.pos.x, potion.pos.y)
