// Lead the peasants and healer through the minefield.

while(true) {
    var coin = hero.findNearestItem();
    var healingThreshold = hero.maxHealth / 2;
    // Check to see if you are critically injured.
    if(hero.health < healingThreshold) {
        // Move left 10m.
        hero.moveXY(hero.pos.x - 10, hero.pos.y);
        // Ask for a heal.
        hero.say("Can I get a heal?");
    // Else, move to the next coin.
    } else if (coin) {
        hero.moveXY(coin.pos.x, coin.pos.y);
    }
}
