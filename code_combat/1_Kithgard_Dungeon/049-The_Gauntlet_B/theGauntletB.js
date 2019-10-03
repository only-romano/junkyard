// Use what you've learned to defeat the ogres.
// Remember: it takes two attacks to defeat an ogre munchkin!

while(true) {
    hero.moveUp();
    var enemy = hero.findNearestEnemy();
    hero.attack(enemy);
    hero.attack(enemy);
}
