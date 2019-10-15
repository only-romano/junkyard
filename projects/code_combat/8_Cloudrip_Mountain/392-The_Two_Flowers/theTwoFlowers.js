// If the peasant is damaged, the flowers will shrink!

function summonSoldiers() {
    if (hero.gold >= hero.costOf("soldier")) {
        hero.summon("soldier");
    }
}

// Define the function: commandSoldiers
function commandSoldiers() {
    var army = hero.findByType("soldier");
    for (var i = 0; i < army.length; i++) {
        var soldier = army[i];
        var enemy = soldier.findNearestEnemy();
        if (enemy && soldier.distanceTo(enemy) < 10) {
            hero.command(soldier, "attack", enemy);
        } else {
            hero.command(soldier, "defend", peasant);
        }
    }
}

// Define the function: pickUpNearestCoin
function pickUpNearestCoin() {
    var coin = hero.findNearestItem();
    if (coin)
        hero.move(coin.pos);
}

var peasant = hero.findByType("peasant")[0];

while(true) {
    summonSoldiers();
    commandSoldiers();
    pickUpNearestCoin();
    
}
