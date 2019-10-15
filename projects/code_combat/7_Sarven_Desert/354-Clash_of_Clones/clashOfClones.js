// You'll need good strategy to win this one!
// Your clone will have the same equipment you have!
// But, they're not very skilled at using special powers

// WARNING - Don't use superpowerful weapon or your clone smash your army up.

while (true) {
    var enemy = hero.findNearestEnemy();
    if (hero.isReady("warcry"))
        hero.warcry();
    if (enemy && enemy.type != "sand-yak") {
        if (hero.canCast("chain-lightning"))
            hero.cast("chain-lightning", enemy);
        else if (hero.isReady("bash"))
            hero.bash(enemy);
    }
}
