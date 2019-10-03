// The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

function chooseStrategy() {
    var enemies = hero.findEnemies();
    // If you can summon a griffin-rider, return "griffin-rider"
    if (hero.gold >= hero.costOf("griffin-rider"))
        return "griffin-rider";
    // If there is a fangrider on your side of the mines, return "fight-back"
    for (var i = 0; i < enemies.length; i++)
        if (enemies[i].type == "fangrider" && enemies[i].pos.x < 55)
            return "fight-back";
    // Otherwise, return "collect-coins"
    return "collect-coins";
}

function commandAttack() {
    // Command your griffin riders to attack ogres.
    var friends = hero.findFriends();
    for (var i = 0; i < friends.length; i++) {
        var friend = friends[i];
        var enemy = friend.findNearestEnemy();
        if (enemy)
            hero.command(friend, "attack", enemy);
    }
}

function pickUpCoin() {
    // Collect coins
    var item = hero.findNearestItem();
    if (item)
        hero.move(item.pos);
}

function heroAttack() {
    // Your hero should attack fang riders that cross the minefield.
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.canCast("regen"))
            hero.cast("regen", hero);
        while (enemy.health > 0)
            hero.attack(enemy);
    }
}

while(true) {
    commandAttack();
    var strategy = chooseStrategy();
    // Call a function, depending on what the current strategy is.
    if (strategy == "griffin-rider")
        hero.summon("griffin-rider");
    else if (strategy == "fight-back")
        heroAttack();
    else {
        commandAttack();
        pickUpCoin();
    }
}
