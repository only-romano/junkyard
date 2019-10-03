// Soldiers will slowly arrive, but the ogres will overwhelm them.
// A basic attack loop isn't going to be enough to keep you alive.
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
