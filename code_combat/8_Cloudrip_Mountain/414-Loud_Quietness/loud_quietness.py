def onHear(event):
    words = event.message.split(" ")
    volume = words[0]
    password = words[1]
    if volume == "Loud":
        pet.say(words[1].toUpperCase())
    if volume == "Quiet":
        pet.say(words[1].toLowerCase())
    pet.moveXY(pet.pos.x+ 24, pet.pos.y)


def passDoor():
    guard = hero.findNearest(hero.findFriends())
    password = guard.password
    if guard.isLoud:
        hero.say(password.toUpperCase())
    elif guard.isQuiet:
        hero.say(password.toLowerCase())
    hero.moveXY(hero.pos.x+ 24, hero.pos.y)


pet.on("hear", onHear)
hero.moveXY(10, 14)
passDoor()
passDoor()
