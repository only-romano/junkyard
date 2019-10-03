// Intercept all ogre messengers from ambush. 

function ambushAttack(target) {
    //  Attack the target if it exists and return to the mark.
    // Write the function:
    if (target) {
        hero.attack(target);
        hero.moveXY(52, 36);
    }
}

while(true) {
    var ogre = hero.findNearestEnemy();
    ambushAttack(ogre);
}
