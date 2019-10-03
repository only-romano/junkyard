penPositions = [{"x":20,"y":24},{"x":28,"y":24},{"x":36,"y":24},{"x":44,"y":24},{"x":52,"y":24}]
penOccupants = [ "empty", "empty", "empty", "empty", "empty" ]
friends = hero.findFriends()

for reindeer in friends:
    for i in range(len(penPositions)):
        penPos = penPositions[i]
        if penPos["x"] == reindeer.pos.x and penPos["y"] == reindeer.pos.y:
            penOccupants[i] = reindeer.id
            break

for i in range(len(penOccupants)):
    hero.say("Pen " + i + " is "  + penOccupants[i])
