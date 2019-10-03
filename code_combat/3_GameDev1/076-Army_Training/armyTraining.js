// Spawn a hero and add a goal.
game.spawnPlayerXY("champion", 40, 15);
game.addDefeatGoal();

// Spawn at least 2 "munchkin"s.
game.spawnXY("munchkin", 30, 30);
game.spawnXY("munchkin", 40, 30);

// Spawn at least 2 "thrower"s.
game.spawnXY("thrower", 50, 50);
game.spawnXY("thrower", 12, 50);

// Spawn at least 2 "soldier"s.
game.spawnXY("soldier", 30, 50);
game.spawnXY("soldier", 30, 20);

// Spawn at least 2 "archer"s.
game.spawnXY("archer", 30, 40);
game.spawnXY("archer", 50, 30);
