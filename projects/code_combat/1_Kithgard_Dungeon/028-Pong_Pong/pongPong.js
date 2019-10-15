// Use all the coding skills you've learned so far to keep the balls from hitting the ground!
// You can hit the balls into the air with the attack() method.
// For a challenge, try to use fewer lines of code.

hero.say("fetch");

while(true) {
    hero.attack("ball2");
    hero.moveRight(3);
    hero.attack("ball2");
    hero.moveLeft(3);
}
