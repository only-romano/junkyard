// That's a lot of Yaks!
// If you are to survive, you'll need to filter out Yaks...

function removeByType(enemies, excludedType) {
    var tempArray = [];
    // Go through each enemy and check to see if its type is excludedType.
    for(var i = 0; i < enemies.length; i++) {
        // If it isn't, 'push' it onto the array.
        var enemy = enemies[i];
        if (enemy.type != excludedType)
            tempArray.push(enemy);
    }
    return tempArray;
}


while(true) {
    // Find the enemies!
    var enemies = hero.findEnemies();
    // Remove those pesky Yaks.
    enemies = removeByType(enemies, "sand-yak");
    var enemy = hero.findNearest(enemies);
    
    // Now... 'remove' those enemies.
    if(enemy) {
        hero.attack(enemy);
    }
}
