// Protect the workers and animals!

// Defend these two positions:
var defend = [];
defend[0] = { x: 98, y: 28 };
defend[1] = { x: 84, y: 7 };

var soldiers = [];

var friends = hero.findFriends();
for(var i=0; i < friends.length; i++) {
    var friend = friends[i];
    if(friend.type == "soldier") {
        soldiers.push(friend);
    } else {
        // Defend the workers:
        defend.push(friend.pos);
    }
}

while(true) {
    // Use a for-loop to assign each soldier to a corresponding defend[] target
    // Use command(soldier, "defend", thang) or command(soldier, "defend", position)
    for (var i = 0; i < soldiers.length; i++) {
        var soldier = soldiers[i];
        var enemy = soldier.findNearestEnemy();
        if (enemy && soldier.distanceTo(enemy) < 5) {
            hero.command(soldier, "attack", enemy);
        } else {
            hero.command(soldiers[i], "defend", defend[i]);
        }
    }
    var enemy = hero.findNearestEnemy();
    if (enemy && hero.distanceTo(enemy) < 10) {
        hero.attack(enemy);
    }
    hero.move({"x": 101, "y": 72});
}
