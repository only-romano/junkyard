// Use a while-true loop to both move and attack.

while (true) {
    hero.moveRight();
    hero.moveUp();
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
    hero.attack(enemy);  // if not enough - repeat it
    hero.moveRight();
    hero.moveDown(2);
    hero.moveUp();
}
