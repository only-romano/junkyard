encodedMessage = hero.findNearest(hero.findFriends()).message
passwordArray = []
passwordLength = 5

words = encodedMessage.split(";")
for word in words:
    word = word.trim()
    if len(word) == passwordLength:
        passwordArray.append(word)

marksPos = [{x: 12, y: 14}, {x: 38, y: 38},
    {x: 42, y: 16}, {x: 54, y: 12}];

for i in range(4):
    pos = marksPos[i]
    hero.moveXY(pos.x, pos.y)
    password = passwordArray[i]
    if password:
        hero.say(password)
    else:
        hero.say("qwerty")
