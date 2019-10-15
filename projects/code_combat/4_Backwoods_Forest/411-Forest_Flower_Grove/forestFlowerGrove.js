// This level is a place for making flower art.
// The real goal is to experiment and have fun!
// If you draw something with at least 1000 flowers, you will *succeed* at the level

var angle = Math.PI / 2;
while (angle < Math.PI * 1.5) {
    hero.moveXY(hero.pos.x + Math.cos(angle), hero.pos.y + Math.sin(angle));
    angle += Math.PI / 96;
}


angle = Math.PI * 1.5;
while (angle < Math.PI * 2.5) {
    hero.moveXY(hero.pos.x + Math.cos(angle), hero.pos.y + Math.sin(angle));
    angle += Math.PI / 124;
}

angle = Math.PI / 2;
while (angle < Math.PI * 1.5) {
    hero.moveXY(hero.pos.x + Math.cos(angle), hero.pos.y + Math.sin(angle));
    angle += Math.PI / 96;
}

angle = Math.PI * 1.5;
while (true) {
    hero.moveXY(hero.pos.x + Math.cos(angle), hero.pos.y + Math.sin(angle));
    angle += Math.PI / 68;
}
