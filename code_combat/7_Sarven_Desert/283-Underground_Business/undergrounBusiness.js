// Accumulate 300 gold and escape from the dungeon.

function onSpawn(event) {
    pet.moveXY(22, 10);
    pet.moveXY(71, 10);
    pet.moveXY(71, 57);
    pet.moveXY(22, 57);
    pet.moveXY(20, 20);
    pet.trick();
}
var items = hero.findItems();
pet.on("spawn", onSpawn);

hero.cast("summon-burl");
hero.cast("summon-undead");
while(true) {
    // Guard peasants:
    var enemy = hero.findNearestEnemy();
    if (enemy) hero.attack(enemy);
    // When you have 300+ gold move to the red mark:
    if (hero.gold >= 290)
        hero.moveXY(50, 34);
}
