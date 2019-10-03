// Use flags to join the battle or retreat.
// If you fail, press Submit again for new random enemies and try again!
// You'll want at least 300 health, if not more.
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
