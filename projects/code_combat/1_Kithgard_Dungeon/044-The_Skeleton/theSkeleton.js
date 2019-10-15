// Use a loop to attack the skeleton.
// Its blunt sword hardly does any damage, but it has huge knockbac
var enemy = hero.findNearestEnemy();
while(true) {
    hero.attack(enemy);
}
