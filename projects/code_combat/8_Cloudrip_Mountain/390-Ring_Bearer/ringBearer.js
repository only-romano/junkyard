// You must escort a powerful magical ring back to town to be studied.
// The goal is to escape, not fight. More ogres lurk in the surrounding mountains!
// Make a circle of soldiers around the peasant!
// We give you two functions to help with this:

// findSoldierOffset figures out the position a soldier should stand at in relation to the peasant.
// The first argument 'soldiers' should be an array of your soldiers.
// The second argument 'i' is the index of the soldier (in soldiers) you want to find the position for.
function findSoldierOffset(soldiers, i) {
    var soldier = soldiers[i];
    var angle = i * 360 / soldiers.length;
    return radialToCartesian(5, angle);
}

// This function does the math to determine the offset a soldier should stand at.
function radialToCartesian(radius, degrees) {
    var radians = Math.PI / 180 * degrees;
    var xOffset = radius * Math.cos(radians);
    var yOffset = radius * Math.sin(radians);
    return {x: xOffset, y: yOffset};
}

var peasant = hero.findByType("peasant")[0];

// Use findByType to get an array of your soldiers.
while(true) {
    // Use a for-loop to iterate over your array of soldiers.
    var soldiers = hero.findByType("soldier");
    for (var i = 0; i < soldiers.length; i++) {
        // Find the offset for a soldier.
        var offset = findSoldierOffset(soldiers, i);
        // Add the offset.x and offset.y to the peasant's pos.x and pos.y.
        var moveTo = {"x": peasant.pos.x + offset.x, "y": peasant.pos.y + offset.y};
        // Command the soldier to move to the new offset position.
        hero.command(soldiers[i], "move", moveTo);
    }
    // The hero should keep pace with the peasant!
    hero.move({x: hero.pos.x + 0.2, y: hero.pos.y});
}
