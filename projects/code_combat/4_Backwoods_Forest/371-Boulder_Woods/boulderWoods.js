// Use isPathClear to move around the randomly positioned boulders.
// Automatic pathfinding doesn't work in Boulder Woods.
while(true) {
    var angle = Math.PI / 2 - Math.PI / 16;
    while (angle >= -Math.PI / 2) {
        var targetX = hero.pos.x + 5 * Math.cos(angle);
        var targetY = hero.pos.y + 5 * Math.sin(angle);
        var target = {"x": targetX, "y": targetY};
        // Use isPathClear between your current `pos` and the target.
        // If the path is clear, move to the target.
        if (hero.isPathClear(hero.pos, target))
            hero.move(target);
        // Otherwise, sweep the `angle` clockwise a bit.
        else
            angle -= Math.PI / 16;
    }
}
