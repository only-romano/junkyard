friendNames = ['Joan', 'Ronan', 'Nikita', 'Augustus']
friendIndex = 0

while friendIndex < len(friendNames):
    friendName = friendNames[friendIndex]
    hero.say(friendName + ', go home!')
    friendIndex += 1

hero.moveXY(20, 30)
hero.buildXY("fence", 30, 30)
