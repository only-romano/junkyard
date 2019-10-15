// Protect the cage.
// Put a soldier at each X.
var points = [];
points[0] = {x: 33, y: 42};
points[1] = {x: 47, y: 42};
points[2] = {x: 33, y: 26};
points[3] = {x: 47, y: 26};

// 1. Collect 80 gold.
while (hero.gold < 80) {
    var item = hero.findNearestItem();
    if (item && item.value)
        hero.move(item.pos);
}

// 2. Build 4 soldiers.
for(var i=0; i < 4; i++) {
    hero.summon("soldier");
}

// 3. Send your soldiers into position.
while(true) {
    var friends = hero.findFriends();
    for(var j=0; j < friends.length; j++) {
        var point = points[j];
        var friend = friends[j];
        var enemy = friend.findNearestEnemy();
        if(enemy && enemy.team == "ogres" && friend.distanceTo(enemy) < 5) {
            // Command friend to attack.
            hero.command(friend, "attack", enemy);
        } else {
            // Command friend to move to point.
            hero.command(friend, "move", point);
        }
    }
}
