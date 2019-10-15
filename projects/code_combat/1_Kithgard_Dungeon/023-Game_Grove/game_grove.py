game.spawnMaze(1)

spewer = game.spawnXY("fire-spewer", 37, 12)
spewer.direction = "horizontal"

gen = game.spawnXY("generator", 26, 44)
gen.spawnType = "munchkin"
gen.spawnDelay = 4

game.spawnXY("munchkin", 28, 19)
game.spawnXY("thrower", 48, 28)

s1 = game.spawnXY("skeleton", 43, 50)
s2 = game.spawnXY("skeleton", 49, 59)
s1.behavior = "Defends"
s2.behavior = "Defends"
game.spawnXY("lightstone", 60, 44)

game.spawnXY("gem", 28, 27)
game.spawnXY("locked-chest", 44, 28)
game.spawnXY("silver-key", 43, 60)
game.spawnXY("potion-medium", 60, 12)

player = game.spawnPlayerXY("samurai", 28, 60)

game.addCollectGoal()
game.addSurviveGoal()

def onVictory(event):
    db.add("defeated", game.defeated)

db.add("plays", 1)
ui.track(db, "plays")
ui.track(db, "defeated")
game.on("victory", onVictory)
