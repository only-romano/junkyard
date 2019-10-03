// Your goal is to protect Reynaldo

// Find the paladin with the lowest health.
function lowestHealthPaladin() {
    var lowestHealth = 99999;
    var lowestFriend = null;
    var friends = hero.findFriends();
    for(var f=0; f < friends.length; f++) {
        var friend = friends[f];
        if(friend.type != "paladin") { continue; }
        if(friend.health < lowestHealth && friend.health < friend.maxHealth) {
            lowestHealth = friend.health;
            lowestFriend = friend;
        }
    }
    return lowestFriend;
}

function commandPaladin(paladin) {
    // Heal the paladin with the lowest health using lowestHealthPaladin()
    // You can use paladin.canCast("heal") and command(paladin, "cast", "heal", target)
    // Paladins can also shield: command(paladin, "shield")
    // And don't forget, they can attack, too!
    var lowest = lowestHealthPaladin();
    var enemy = paladin.findNearestEnemy();
    if (paladin.canCast("heal") && lowest)
        hero.command(paladin, "cast", "heal", lowest);
    else if (enemy && paladin.health > paladin.maxHealth * 0.5)
        hero.command(paladin, "attack", enemy);
    else
        hero.command(paladin, "shield");
}

function commandFriends() {
    // Command your friends.
    var friends = hero.findFriends();
    for(var i=0; i < friends.length; i++) {
        var friend = friends[i];
        if(friend.type == "peasant") {
            //commandPeasant(friend);
            commandPeasant(friend);
        } else if(friend.type == "griffin-rider") {
            //commandGriffin(friend);
            commandGriffin(friend);
        } else if(friend.type == "paladin") {
            commandPaladin(friend);
        }
    }
}

function commandGriffin(griffin) {
    var enemy = griffin.findNearestEnemy();
    if (enemy)
        hero.command(griffin, "attack", enemy);
}

function commandPeasant(peasant) {
    var item = peasant.findNearestItem();
    if (item)
        hero.command(peasant, "move", item.pos);
}

function summonGriffins() {
    if (hero.gold >= hero.costOf("griffin-rider"))
        hero.summon("griffin-rider");
}

while(true) {
    commandFriends();
    // Summon griffin riders!
    summonGriffins();
}
