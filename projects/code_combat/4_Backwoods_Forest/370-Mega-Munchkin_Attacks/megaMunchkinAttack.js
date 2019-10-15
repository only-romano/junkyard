// That's a big'un! With some clever thinking, Ivy should be able to take care of this situation single-handedly.

while(true) {
    // Find the archer.
    var friend = hero.findNearest(hero.findFriends());
    var enemy = hero.findNearest(hero.findEnemies());
    
    // Tell the archer to attack the enemy!
    // Wait, no, that doesn't work that well. Maybe try something else?
    // The munchkin is awfully slow...
    if(friend && enemy) {
        hero.command(friend, "attack", enemy);
        if (friend.pos.x + 8 > enemy.pos.x) {
            hero.command(friend, "move", {"x": enemy.pos.x - 15, "y": friend.pos.y - 7});
        }
    }
}
