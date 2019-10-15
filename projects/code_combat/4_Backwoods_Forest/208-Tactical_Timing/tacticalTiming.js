// Help out on the front line.
// Move back to a flag if any try to sneak by.

while (true) {
    var enemy = hero.findNearestEnemy();
    var flag = hero.findFlag();

    if (flag) {
        hero.pickUpFlag(flag);
    } else if (enemy) {
         var distance = hero.distanceTo(enemy);

        if (distance <= 30) {
            hero.attack(enemy);
        }
    }
}
