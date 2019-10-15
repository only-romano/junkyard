// You can't reach your friends to defend them!
// Tell them to go home where the archer can help.

while (true) {
    var weakestFriend = null;
    var leastHealth = 9999;
    var friendIndex = 0;
    var friends = hero.findFriends();
    // Find which friend has the lowest health.
    while (friendIndex < len(friends)) {
        var friend = friends[friendIndex];
        friendIndex += 1;
        if (friend.health < leastHealth) {
            weakestFriend = friend;
            leastHealth = friend.health;
        }
    }
    // Tell the weakest friends to go home first.
    if (weakestFriend)
        hero.say('Hey ' + weakestFriend.id + ', go home!');
}
