// You should recognize this from the last level.
hero.moveRight();
while (true) {
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
    hero.attack(enemy);

    hero.moveRight(2);
}
