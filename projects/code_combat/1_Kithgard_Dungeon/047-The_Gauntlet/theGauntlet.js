// Use what you've learned to defeat the ogres.
// Remember: it takes two attacks to defeat an ogre munchkin!

while(true) {
    hero.moveRight();
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
    hero.attack(enemy);
}
