// We should quickly build a fort!

// The foreman stored the list of workers' names as a property.
var foreman = hero.findNearest(hero.findFriends());
var workerNameList = foreman.workerList;


// Use loops with steps to choose each third element.
// First, you need assign workers for the towers.
// Use start value 1 and increase the index by 3.
for (var i = 1; i < workerNameList.length; i += 3) {
    // For each of them say the name and what to build.
    hero.say(workerNameList[i] + " - tower");
}

// First, you need assign workers for the tents.
// Use start value 0 and increase the index by 3.
for (i = 0; i < workerNameList.length; i += 3) {
    // For each of them say to build "tent".
    hero.say(workerNameList[i] + " - tent");
}

// Finally, you need assign workers for the fence.
// Use start value 2 and increase the index by 3.
for (i = 2; i < workerNameList.length; i += 3) {
    // For each of them say to build "fence".
    hero.say(workerNameList[i] + " - fence");
}

// Now watch for the battle or help your army.

while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy)
        hero.attack(enemy);
}
