// There may be something around to help you!
// First, move to the Cupboard.
for (var i = 0; i < 2; i++) {
    hero.moveRight();
    hero.moveDown();
}
hero.moveDown();

// Then, attack the "Cupboard" inside a while-true loop.
while(true) {
    hero.attack("Cupboard");
}
