// Use charges to soften up packs of ogres.
// Then pick them off with your bow.

while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.isReady("throw")) {
            var distance = hero.distanceTo(enemy);
            // Only throw if the ogres are more than 15m away.
            // Use "if" to compare distance to 15.
            if (distance > 15) {
                hero.throw(enemy);
            }
            // Use "else" to attack if you're not throwing.
            else {
                hero.attack(enemy);
            }
        }
        else {
            hero.attack(enemy);
        }
    }
}
