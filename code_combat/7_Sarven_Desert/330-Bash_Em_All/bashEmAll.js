// Be careful with these ogres.
// They are special trained fat-free uber ogres and very strong.
// The keyword is fat-free.w

while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy && enemy.health > 0) {
        if (hero.isReady("bash")) {
            hero.bash(enemy);
            hero.moveXY(40, 33);
        }
        else
            hero.shield();
    } else {
        hero.moveXY(18, 9);
        hero.moveXY(66, 58);
        hero.moveXY(40, 33);
        hero.moveXY(63, 14);
        hero.moveXY(15, 56);
    }
}
