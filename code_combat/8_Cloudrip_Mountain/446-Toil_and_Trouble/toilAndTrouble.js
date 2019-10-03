// Ogre Witches have some unpleasant surprises ready for you.

// Define a chooseTarget function which takes a friend argument
// Returns the a target to attack, depending on the type of friend.
// Soldiers should attack the witches, archers should attack nearest enemy.
function chooseTarget(friend) {
    if (friend.type == "soldier") {
        var enemy = friend.findNearest(hero.findByType("witch"));
        if (enemy)
            return enemy;
    }

    return friend.findNearestEnemy();
}


while(true) {
    var friends = hero.findFriends();
    for(var i=0; i < friends.length; i++) {
        // Use your chooseTarget function to decide what to attack.
        var friend = friends[i];
        var enemy = chooseTarget(friend);
        if (enemy)
            hero.command(friend, "attack", enemy);
    }
}
