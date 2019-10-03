while True:
    green = hero.findFlag("green")
    black = hero.findFlag("black")
    nearest = hero.findNearestEnemy()
    
    if green:
        hero.pickUpFlag(green)
    elif black and hero.isReady("cleave")
        hero.pickUpFlag(black)
        hero.cleave(nearest)
    elif nearest and hero.distanceTo(nearest) < 10
        hero.attack(nearest);
