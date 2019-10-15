// Collect 9 mushrooms.

// This function makes the pet fetch potions for you.
function onSpawn(event) {
    while(true) {
        // Pets can find the nearest item by its type.
        var potion = pet.findNearestByType("potion");
        // Make the pet fetch the potion if it exists:
        pet.fetch(potion);
    }
    
}
pet.on("spawn", onSpawn);

// Mushrooms are toxic, don't collect them too quickly.
while(true) {
    var someItem = hero.findNearestItem();
    if (someItem && hero.health > hero.maxHealth / 3) {
        // Collect the someItem:
        hero.move(someItem.pos);
    }
}
