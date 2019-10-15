// Free the prisoner, defeat the guard and grab the gem.
hero.moveRight();

// Free Patrick from behind the "Weak Door".
hero.attack("Weak Door");
hero.moveRight(2);

// Defeat the guard, named "Two".
hero.attack("Two");
hero.attack("Two");

// Get the gem.
hero.moveDown(3);
hero.moveRight();
