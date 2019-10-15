// There may be something around to help you!
hero.moveUp();

// First, move to the Cupboard.
hero.moveRight(2);
hero.moveDown(2);

// Then, attack the "Cupboard" inside a while-true loop.
while(true)
    hero.attack("Cupboard");
