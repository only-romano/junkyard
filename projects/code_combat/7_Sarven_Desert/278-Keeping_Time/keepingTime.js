// Use your new skill to choose what to do: hero.time

function getItems() {
    var item = hero.findNearestItem();
    if (item)
        hero.moveXY(item.pos.x, item.pos.y);
}

function manualAttack() {
    var enemy = hero.findNearestEnemy();
    if (enemy)
        hero.attack(enemy)
}

while(true) {
    // If it's the first 10 seconds, attack.
    if (hero.time < 10) {
        manualAttack();
    }
    // Else, if it's the first 35 seconds, collect coins.
    else if (hero.time < 35)
        getItems();
    // After 35 seconds, attack again!
    else
        manualAttack();
}
