def findFriendByName(name):
    friends = hero.findFriends()
    for friend in friends:
        if friend.id == name:
            return friend
    return None


sergeant = hero.findNearest(hero.findFriends())
wereList = sergeant.wereList
wereNames = wereList.split(",")

for name in wereNames:
    trimmedName = name.strip()
    friend = findFriendByName(trimmedName)
    hero.command(friend, "move", {"x": 48, "y": 48})
