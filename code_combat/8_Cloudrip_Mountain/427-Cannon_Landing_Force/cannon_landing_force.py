landingMap = hero.findNearest(hero.findFriends()).landingMap

cell = landingMap[0][0]
hero.say("row 0 column 0 " + cell)
hero.say("row 3 column 2 " + landingMap[3][2])
hero.say("row 2 column 1 " + landingMap[2][1])
hero.say("row 1 column 0 " + landingMap[1][0])
hero.say("row 0 column 2 " + landingMap[0][2])
hero.say("row 1 column 3 " + landingMap[1][3])
