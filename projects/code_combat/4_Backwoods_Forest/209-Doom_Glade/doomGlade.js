// An ogre army approaches. Use flags to win the battle!
// It's important to good flag using!


while (true) {
    var flag = hero.findFlag();
    if (flag)
        hero.pickUpFlag(flag);
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.isReady("cleave") && hero.distanceTo(enemy) < 5)
            hero.cleave(enemy);
        else if (hero.isReady("bash"))
            hero.bash(enemy);
        else hero.attack(enemy);
    }
    if (hero.findEnemies().length > 10)
        hero.shield();
}
