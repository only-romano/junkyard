def findByName(name, thangs):
    for thang in thangs:
        if thang.id == name:
            return thang
    return None


friends = hero.findFriends()
celadia = findByName("Celadia", friends)
dedalia = findByName("Dedalia", friends)
sideLength = celadia.distanceTo(dedalia)

vaelia = findByName("Vaelia", friends)
illumina = findByName("Illumina", friends)

hero.command(vaelia, "move", {"x": celadia.pos.x, "y": celadia.pos.y - sideLength})
hero.command(illumina, "move", {"x": dedalia.pos.x, "y": dedalia.pos.y - sideLength})
