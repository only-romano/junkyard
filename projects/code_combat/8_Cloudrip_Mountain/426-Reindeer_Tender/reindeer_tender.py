penPositions = [ {"x":20,"y":24}, {"x":28,"y":24}, {"x":36,"y":24}, {"x":44,"y":24}, {"x":52,"y":24} ]
penOccupants = [ None, None, None, None, None ]
friends = hero.findFriends()

for i in range(len(friends)):
    reindeer = friends[i]
    for j in range(len(penPositions)):
        penPos = penPositions[j]
        if penPos["x"] == reindeer.pos.x and penPos["y"] == reindeer.pos.y:
            penOccupants[j] = reindeer
            friends[i] = None
            break

for reindeer in friends:
    if not reindeer:
        continue
    for i in range(len(penOccupants)):
        if penOccupants[i] == None
            penOccupants[i] = reindeer
            hero.command(reindeer, "move", penPositions[i])
            break
