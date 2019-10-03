// Defeat the skeleton and open the chest.

function onSpawn (event) {
    // Pet should find the health potion (type is "potion"): 
    var potion = pet.findNearestByType("potion");
    // and fetch it:
    if (potion) pet.fetch(potion);
    // Pet should find the gold key (type is "gold-key"):
    var goldKey = pet.findNearestByType("gold-key");
    // and fetch it:
    if (goldKey) pet.fetch(goldKey);
}

// Pet can find more than just items:
var skeleton = pet.findNearestByType("skeleton");
pet.on("spawn", onSpawn);

while(true) {
    if (skeleton.health > 0 && !hero.hasEffect("hide"))
        hero.attack(skeleton);
    else if (skeleton.health <= 0)
        hero.moveXY(31, 38);
}
