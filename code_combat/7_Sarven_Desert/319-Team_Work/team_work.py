items = hero.findItems()

gem0 = items[0]
hero.say("Bruno " + gem0)
hero.say("Matilda " + items[1])
gem1 = items[2]
hero.moveXY(gem1.pos.x, gem1.pos.y)
