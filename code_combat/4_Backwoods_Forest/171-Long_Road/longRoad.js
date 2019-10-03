// Move to the right.

// Complete this function:
function onSpawn(event){
    // Inside a while-true loop:
    while(true) {
        
        // Use hero.findNearestItem()
        var item = hero.findNearestItem();
        // If there's an item:
        if (item) {
            // Use pet.fetch(item) to fetch the item.
            pet.fetch(item);
        }
    }
}

// Use pet.on() to assign onSpawn to the "spawn" event
pet.on("spawn", onSpawn);
hero.moveXY(78, 35);
