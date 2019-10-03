// Goal: build three rows of nine fire-traps.

// Returns "retreat", "attack", "start-next-trap-column", or "build-next-trap-in-column"
function chooseStrategy() {
    var enemies = hero.findEnemies();

    // If there are overwhelming ogre forces, return the "retreat" strategy.
    if(enemies.length > 20) {
        return "retreat";
    } 
    // If there are some ogres, return the "attack" strategy.
    else if (enemies.length > 0) {
        return "attack";
    }
    // Use x % 9 === 0 to see if x is divisible by 9.
    // Use this.built.length to see how many traps you have built.
    // If you have finished a column of 9 traps, return "start-next-trap-column"
    else if (hero.built.length % 9 === 0) {
        return "start-next-trap-column";
    }
    // Otherwise, return "build-next-trap-in-column"
    else {
        return "build-next-trap-in-column";
    }
}

var trapsInColumn = 9;
var startX = 40;
var columnX = startX;

// Build the next trap in a column in the correct place.
function buildNextTrapInColumn(columnX,numTraps) {
    // Change newY to use % to wrap around and only build trapsInColumn (9) traps per column
    var newY = 7 * (numTraps % 9) + 10; // ∆ Change this to use % 9!
    if (hero.pos.y < newY) {
        hero.move({"x": columnX - 5, "y": newY});
    } else {
        buildTrap(columnX,newY);
    }
}

// Start a new column of traps.
function startNextTrapColumn(columnX, numTraps) {
    var newX = startX - (Math.floor(numTraps / trapsInColumn) * 6);
    if (hero.pos.y > 10) {
        hero.move({"x": newX - 5, "y": 10});
        return columnX;
    } else {
        buildTrap(newX,10);
        return newX;
    }
}

function buildTrap(x, y) {
    hero.buildXY("fire-trap", x, y);
}


function commandAttack() {
    // Have your griffin riders fend off the attackers.
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        var enemy = friend.findNearestEnemy();
        if (enemy)
            hero.command(friend, "attack", enemy);
    }
}

function commandRetreat() {
    hero.say("Retreat!");
    // You and your griffin riders retreat to safety behind the traps.
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        hero.command(friend, "move", {x: 10, y: friend.pos.y});
    }
    hero.moveXY(8, 42);
}


while(true) {
    var strategy = chooseStrategy();
    if(strategy == "attack") {
        commandAttack();
    } else if(strategy == "build-next-trap-in-column") {
        buildNextTrapInColumn(columnX, hero.built.length);
    } else if(strategy == "start-next-trap-column") {
        columnX = startNextTrapColumn(columnX, hero.built.length);
    } else if(strategy == "retreat") {
        commandRetreat();
    }
}

