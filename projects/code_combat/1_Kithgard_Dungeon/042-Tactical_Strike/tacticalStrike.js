// Defeat the ogres.
hero.moveUp();
hero.moveRight(3);
hero.moveDown(2);

for (var i = 0; i < 2; i++) {
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
    hero.attack(enemy);
}

hero.moveLeft();
hero.moveDown();
