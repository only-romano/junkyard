// Our wizards teleport ogres from their camp here.
// They appear for a short period and they are stunned.
// Attack only weak and near ogres.

while (true) {
    var enemy = hero.findNearestEnemy();
    var distance = hero.distanceTo(enemy);
    // If enemy.type is "munchkin"
    // AND the distance to it is less than 20m
    if (enemy.type == "munchkin" && distance < 20) {
        // Then attack it.
        hero.attack(enemy);
    }
}
