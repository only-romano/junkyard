while True:
    item = hero.findNearestItem()
    if item and item.type != "gem":
            hero.moveXY(pet.pos.x, pet.pos.y)
        else:
            hero.moveXY(item.pos.x, item.pos.y)
