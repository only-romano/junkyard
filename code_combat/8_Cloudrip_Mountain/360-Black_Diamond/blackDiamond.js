while(true) {
    var gem = hero.findNearest(hero.findItems());
    if (gem) {
        var clear = hero.isPathClear(hero.pos, gem.pos);
        // The isPathClear method tells you if there’s an obstacle in the way.
        // If it’s clear, move() to gem.pos.
        if (clear)
            hero.move(gem.pos);
        // Else, move back to the center point.
        else
            hero.move({"x": 40, "y": 35});
    }
}
