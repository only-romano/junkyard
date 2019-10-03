// This array contains friends and ogres.
// The even elements are ogres, but the odds are friends.
var everybody = ['Yetu', 'Tabitha', 'Rasha', 'Max', 'Yazul',  'Todd'];
var enemyIndex = 0;

while (enemyIndex < everybody.length) {
    // Use square brackets to get the ogre name from the array.
    var ogre = everybody[enemyIndex];
    // Attack using the variable holding the ogre name.
    if (hero.isReady("bash")) hero.bash(ogre);
    else hero.attack(ogre);
    // Increment by 2 to skip over friends.
    enemyIndex += 2;
}

// After defeating ogres, move to the oasis.
hero.moveXY(35, 54);
