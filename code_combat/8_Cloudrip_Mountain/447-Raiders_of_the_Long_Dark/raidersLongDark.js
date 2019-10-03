// Your goal is to protect the peasant and move to the right.
// Arryn Stonewall will defend the front, and command the soldiers.
// You need to cover the rear and command the peasant.

var arryn = hero.findByType("raider")[0];
var peasant = hero.findByType("peasant")[0];

function chooseHeroStrategy() {
    // Return either "fight" or "advance".
    // Try to stay 5m behind the peasant when not fighting.
    // Don't get more than 15m away from the peasant.
    var enemy = hero.findNearestEnemy();
    if (enemy && hero.distanceTo(enemy) <= 5 && hero.distanceTo(peasant) < 15)
        return "fight";
    return "advance";
}

function heroFight() {
    // Stop the ogres from rushing past you to get to the peasant!
    // Hint: try to slow them down if you can
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.isReady("bash"))
            hero.bash(enemy);
        else
            hero.attack(enemy);
    }
}

function heroAdvance() {
    // Stay behind the peasant
    hero.move({x: peasant.pos.x - 5, y: peasant.pos.y});
}

function choosePeasantStrategy() {
    // Return "follow", "build-above", or "build-below"
    // Hint: use isPathClear() to determine where the hallways are
    if (hero.isPathClear(peasant, {x: peasant.pos.x, y: peasant.pos.y + 8}))
        return "build-above";
    if (hero.isPathClear(peasant, {x: peasant.pos.x, y: peasant.pos.y - 8}))
        return "build-below";
    return "follow";
}

function peasantAdvance() {
    // Keep the peasant behind Arryn and her soldiers.
    hero.command(peasant, "move", {x: arryn.pos.x - 5, y: arryn.pos.y});
}

function peasantBuild(x,y) {
    // Command the peasant to build a palisade.
    hero.command(peasant, "buildXY", "palisade", x, y);
}

while(true) {
    var heroStrategy = chooseHeroStrategy();
    if(heroStrategy == "fight") {
        heroFight();
    } else if(heroStrategy == "advance") {
        heroAdvance();
    }
    
    var peasantStrategy = choosePeasantStrategy();
    if(peasantStrategy == "build-above") {
        peasantBuild(peasant.pos.x, peasant.pos.y + 5);
    } else if(peasantStrategy == "build-below") {
        peasantBuild(peasant.pos.x, peasant.pos.y - 5);
    } else if(peasantStrategy == "follow") {
        peasantAdvance();
    }
}
