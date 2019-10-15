// Collect 80 gold
while (hero.gold < 80) {
    var item = hero.findNearestItem();
    if (item)
        hero.move(item.pos)
}

// Build 4 soldiers to use as bait
for (var i = 0; i < 4; i++) {
    hero.summon("soldier");
}

// Send your soldiers into position
var points = [];
points[0] = { x: 13, y: 73 };
points[1] = { x: 51, y: 73 };
points[2] = { x: 51, y: 53 };
points[3] = { x: 90, y: 52 };
var friends = hero.findFriends();

// Use a for-loop to loop over i from 0 to 4
// Match the friends to the points and command them to move
for (var i = 0; i < 4; i++) {
    var friend = friends[i];
    var point = points[i];
    hero.command(friend, "move", point);
}
