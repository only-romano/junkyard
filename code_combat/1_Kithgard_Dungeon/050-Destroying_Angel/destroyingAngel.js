hero.moveDown();

// Mama always said to eat random mushrooms you find in dungeons.
hero.moveRight();
hero.moveDown();
hero.moveUp();
hero.moveLeft();
hero.moveDown(2);


// Find your way to the Dungeon Keeper.
hero.moveRight(4);
hero.moveUp();
hero.moveLeft();
hero.moveUp();
hero.moveRight();
hero.moveLeft();
hero.moveUp();
hero.moveRight();


while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
    }
}
