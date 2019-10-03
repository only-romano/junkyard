while hero.gold < 80:
    item = hero.findNearestItem()
    if (item)
        hero.move(item.pos)

for i in range(4):
    hero.summon("soldier")

points = []
points[0] = { x: 13, y: 73 }
points[1] = { x: 51, y: 73 }
points[2] = { x: 51, y: 53 }
points[3] = { x: 90, y: 52 }
friends = hero.findFriends()

for i in range(len(friends)):
    hero.command(friends[i], "move", points[i])
