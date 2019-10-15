while(true) {
    // Collect gold.
    var coin = hero.findNearestItem();
    if (coin)
        hero.move(coin.pos);
    // If you have enough gold, summon a soldier.
    if (hero.gold >= hero.costOf("soldier"))
        hero.summon("soldier");
    // Use a for-loop to command each soldier.
    var friends = hero.findFriends();
    var heal = [];

    for(var friendIndex = 0; friendIndex < friends.length; friendIndex++) {
        var friend = friends[friendIndex];
        if(friend.type == "soldier") {
            var enemy = friend.findNearestEnemy();
            // If there's an enemy, command her to attack.
            // Careful! If your soldiers are defeated, a warlock will appear!
            // Otherwise, move her to the right side of the map.
            if (enemy) {
                if (friend.health < 100) {
                    hero.command(friend, "move", {"x": 20, "y": 48});
                    heal.push(friend);
                } else
                    hero.command(friend, "attack", enemy);
            } else {
                hero.command(friend, "move", {"x": 80, "y": 48});
            }
            
        }
    }

    if (hero.canCast("regen")) {
        for (var i = 0; i < heal.length; i++) {
            if (hero.distanceTo(heal[i]) <= 30) {
                hero.cast("regen", heal[i]);
                break;
            }
        }
    }
}
