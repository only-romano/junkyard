// Escape from the maze by moving to the X mark.
// Try to collect as many coins as you can.
hero.attack("Treasure Chest");
hero.moveUp();
hero.moveDown();
hero.moveRight();
hero.attack("Gate");
hero.moveUp(2);
hero.moveDown(2);
hero.moveLeft(3);

while(true) {
    hero.moveUp(2);
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
    hero.moveLeft(2);
    hero.moveRight(2);
    hero.moveDown();
    hero.moveRight();
    hero.moveUp();
    hero.moveRight();
}

