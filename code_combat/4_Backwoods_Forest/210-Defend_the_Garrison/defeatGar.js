// Defeat all of the attacking ogres.
// Use flags to move away from dangerous ogres.

while (true) {
    var flag = hero.findFlag();
    if (flag)
        hero.pickUpFlag(flag);
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.canCast("chain-lightning")) hero.cast("chain-lightning", enemy);
        else if (hero.isReady("electrocute")) hero.electrocute(enemy);
        else if (hero.isReady("cleave") && (hero.distanceTo(enemy) < 5)) hero.cleave(enemy);
        else if (hero.isReady("bash")) hero.bash(enemy);
        else hero.shield();
    }
}
