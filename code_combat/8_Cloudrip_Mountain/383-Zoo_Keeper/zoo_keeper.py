points = [];
points[0] = {x: 33, y: 42};
points[1] = {x: 47, y: 42};
points[2] = {x: 33, y: 26};
points[3] = {x: 47, y: 26};

while hero.gold < 80:
    item = hero.findNearestItem()
    if item && item.value:
        hero.move(item.pos)

for i in range(4):
    hero.summon("soldier")

while True:
    friends = hero.findFriends()
    for j in range(len(friends)):
        point = points[j]
        friend = friends[j]
        enemy = friend.findNearestEnemy()
        if enemy and enemy.team == "ogres" and friend.distanceTo(enemy) < 5:
            hero.command(friend, "attack", enemy)
        else:
            hero.command(friend, "move", point)
