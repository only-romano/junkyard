// Ogres are attacking a nearby outpost!
// Command the hero to defend the tiny settlement.
// Time your patrol with a watch so no ogres can get through.

while(true) {
    var polarPos = hero.time / 4;
    // Number between 20 and 60.
    var xPos = 40 + Math.cos(polarPos) * 20;
    // Number between 14 and 54.
    var yPos = 34 + Math.sin(polarPos) * 20;
    hero.moveXY(xPos, yPos);
    // Check for ogres and defeat them!
    // Make sure to attack while their health is above 0.
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        while (enemy.health > 0) {
            if (hero.canCast("chain-lightning"))
                hero.cast("chain-lightning", enemy);  // fix for weak heroes required Emperor's gloves
            else
                hero.attack(enemy);
        }
    }
}
