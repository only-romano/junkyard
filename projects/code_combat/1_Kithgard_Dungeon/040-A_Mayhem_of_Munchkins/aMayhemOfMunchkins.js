// Inside a while-true loop, use findNearestEnemy() and attack!
while(true) {
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
}
