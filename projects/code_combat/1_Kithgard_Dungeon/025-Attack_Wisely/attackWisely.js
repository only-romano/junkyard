// Don't step on fire traps!
hero.moveUp(2);
hero.attack("Door A");
hero.attack("Door A");
hero.moveUp(3);

var enemy = hero.findNearestEnemy();
hero.attack(enemy);
hero.attack(enemy);  // if it's not enough repeat this line

hero.moveDown(3);
hero.moveRight(2);

// Some ogres are stronger than others!
// Only defeat the ogres you can easily handle.
// Attack doors by name and ogres with findNearestEnemy.

hero.moveUp(1);
hero.attack("Door B");
hero.attack("Door B");
hero.moveUp(3);

enemy = hero.findNearestEnemy();
hero.attack(enemy);
hero.attack(enemy);  // if it's not enough repeat this line

hero.moveDown(2);
hero.moveRight(2);

hero.attack("Door C");
hero.attack("Door C");
hero.moveUp(3);

enemy = hero.findNearestEnemy();
hero.attack(enemy);
hero.attack(enemy);  // if it's not enough repeat this line

hero.moveDown(2);
hero.moveRight(2);
hero.moveUp(2);

enemy = hero.findNearestEnemy();
hero.attack(enemy);
hero.attack(enemy);  // if it's not enough repeat this line

enemy = hero.findNearestEnemy();
hero.attack(enemy);
hero.attack(enemy);  // if it's not enough repeat this line


// When you're done, escape (move to the x-mark).

hero.moveRight();
hero.moveDown(3);
hero.moveLeft(5);
hero.moveDown(2);
