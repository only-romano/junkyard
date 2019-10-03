# You need a high-level boots to access a "move" action
# You need the Emperor's gloves to cast "Chain Lightning"
# You need the Unholy Tome IV+ to cast strong enough "Drain Life"

def onSpawn():
    item = hero.findNearestItem()
    if item:
        pet.fetch(item)


whiteX = {x:27, y:42}
redX = {x:151 , y: 118}
pet.on("spawn", onSpawn)

traps = hero.findHazards()
max = 0
min = 9999

for trap in traps:
    value = trap.value
    if value:
        if value < min:
            min = value
        if value > max:
            max = value

hero.moveXY(whiteX.x, whiteX.y)
hero.say(min + max)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.canCast("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        else:
            hero.cast("drain-life", enemy)
    hero.move(redX);
