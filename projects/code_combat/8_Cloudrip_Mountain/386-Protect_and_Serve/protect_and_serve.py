defend = []
defend[0] = { x: 98, y: 28 }
defend[1] = { x: 84, y: 7 }
soldiers = []

friends = hero.findFriends()
for friend in friends:
    if friend.type == "soldier":
        soldiers.push(friend)
    else:
        defend.push(friend.pos)

while True:
    for soldier in soldiers:
        enemy = soldier.findNearestEnemy()
        if enemy and soldier.distanceTo(enemy) < 5:
            hero.command(soldier, "attack", enemy)
        else:
            hero.command(soldiers[i], "defend", defend[i])
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        hero.attack(enemy)
    hero.move({"x": 101, "y": 72})
