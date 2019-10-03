// Sneak through the forest and ambush the shaman.
// Listen to 'Commander Craig' for warning of approaching enemy.
// Place flags after pressing Submit.
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
