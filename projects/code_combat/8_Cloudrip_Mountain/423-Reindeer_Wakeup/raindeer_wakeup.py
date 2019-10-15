deerStatus = [ "asleep", "asleep", "asleep", "asleep", "asleep" ]
friends = hero.findFriends()

for i in range(len(friends)):
    if friends[i].pos.y > 30:
        deerStatus[i] = "awake"

for i in range(len(deerStatus)):
    hero.say("Reindeer " + i + " is " + deerStatus[i])
