// Senick needs big bait for a big burl!
// Help Senick find an above average yak!
// Don't pick one too deep in the herd, or risk angering the group.

// This function should return the average size of all the yaks:
function averageSize(yaks) {
    var sum = 0;
    // Go through each yak and add its size to the sum.
    for (var i = 0; i < yaks.length; i++)
        sum += yaks[i].size;
    return sum / yaks.length;
}

var yaks = hero.findEnemies();
var avgSize = averageSize(yaks);

var bestYak = null;
var closestDist = Infinity;
for(var i = 0; i < yaks.length; i++) {
    var yak = yaks[i];
    var yakDistance = hero.distanceTo(yak);
    var yakSize = yak.size;
    // Check if the yak is:
    // The distance is closer than the current 'closestDist' AND
    // The size is bigger than the 'avgSize'.
    if (yakDistance < closestDist && yakSize > avgSize) {
        // Update the 'bestYak' and 'closestDist'
        bestYak = yak;
        closestDist = yakDistance;
    }
}
// Say the 'bestYak':
hero.say(bestYak);