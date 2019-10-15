// Get three keys and free the paladin.

function onSpawn(event) {
    // The pet should find and fetch three keys.
    // You need items with the next types:
    // "bronze-key", "silver-key" and "gold-key".
    var key = pet.findNearestByType("bronze-key");
    if (key) pet.fetch(key);
    key = pet.findNearestByType("silver-key");
    if (key) pet.fetch(key);
    key = pet.findNearestByType("gold-key");
    if (key) pet.fetch(key);
}

pet.on("spawn", onSpawn);

while(true) {
    var enemy = hero.findNearestEnemy();
    if (enemy && enemy.team == "ogres") {
        hero.attack(enemy);
    }
    if (hero.health < 300) {
        // You can use pets in the main thread too.
        var potion = pet.findNearestByType("potion");
        if (potion) {
            hero.moveXY(potion.pos.x, potion.pos.y);
        }
    }
}
