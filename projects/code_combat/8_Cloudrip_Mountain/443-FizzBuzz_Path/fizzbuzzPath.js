// Be aware of hidden traps, and count your steps
// Coins are separated by 10 meters distance

var steps = 1;

while (true) {
    // If the number of steps is divisible by 3 AND by 5 -- move to North-West
    if (steps % 3 === 0 && steps % 5 === 0)
        hero.moveXY(hero.pos.x - 10, hero.pos.y + 10);
    // Else if the number of steps is divisible by 3 -- move to East
    else if (steps % 3 === 0)
        hero.moveXY(hero.pos.x + 10, hero.pos.y);
    // Else if the number of steps is divisible by 5 -- move to West
    else if (steps % 5 === 0)
        hero.moveXY(hero.pos.x - 10, hero.pos.y);
    // Else move to North
    else
        hero.moveXY(hero.pos.x, hero.pos.y + 10);
    
    steps += 1;
}
