// The hot sun is draining the hero's health!

while (true) {
    var enemy = hero.findNearestEnemy();
    // Attack if enemy exists AND enemy.team is "ogres"
    // AND enemy.type is "skeleton"
    if (enemy && enemy.team === "ogres" && enemy.type === "skeleton") {
        hero.attack(enemy);
    }
    
    var item = hero.findNearestItem();
    // Collect if item exists AND item.type is "potion"
    // AND hero.health is less than hero.maxHealth / 4
    if (item && item.type == "potion" && hero.health < hero.maxHealth / 4)
        hero.moveXY(item.pos.x, item.pos.y);
}
