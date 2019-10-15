// Ogres are going to attack soon.
// Move near each of tents (to the X marks)
// say() something at each X to wake your soldiers.
// Beware: leave the camp when the battle begins!
// Ogres will send reinforcements if they see the hero.

// The sergeant knows the distance between tents.
var sergeant =  hero.findNearest(hero.findFriends());

// The distances between the X marks.
var stepX = sergeant.tentDistanceX;
var stepY = sergeant.tentDistanceY;
// The number of tents.
var tentsInRow = 5;
var tentsInColumn = 4;

// The first tent mark has constant coordinates.
var firstX = 10;
var firstY = 14;

var finalX = firstX + tentsInRow * stepX;
var finalY = firstY + tentsInColumn * stepY;

// Use nested loops and visit all 20 tents.
// IMPORTANT: move row by row - it's faster.
for (var y = firstY; y < finalY; y += stepY) {
    for (var x = firstX; x < finalX; x += stepX) {
        // Move at the marks near tents and say anything.
        hero.moveXY(x, y);
        hero.say("War!");
    }
}
// Now watch the battle.
while (true) {
    var friend = hero.findNearest(hero.findFriends());
    if (friend && hero.canCast("grow"))
        hero.cast("grow", friend);
    if (friend && hero.canCast("regen"))
        hero.cast("regen", friend);
}
