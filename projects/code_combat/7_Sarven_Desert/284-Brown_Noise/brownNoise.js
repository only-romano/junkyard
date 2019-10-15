// Collect the treasure and escape.

// Prepare the hero and the pet.
pet.moveXY(32, 28);
hero.moveXY(10, 19);
var enemy = hero.findNearestEnemy();
pet.distractionNoise();
hero.backstab(enemy);
hero.moveXY(10, 46);

// Repeat this maneuver to get the treasure:
hero.moveXY(46, 40);
pet.moveXY(64, 28);
pet.distractionNoise();
hero.jumpTo({x:45, y:9});
hero.moveXY(70, 9);
hero.moveXY(45, 9);
pet.distractionNoise();
hero.jumpTo({x:46, y:40});

// Escape from the dungeon (the red mark):
hero.moveXY(40, 56);

