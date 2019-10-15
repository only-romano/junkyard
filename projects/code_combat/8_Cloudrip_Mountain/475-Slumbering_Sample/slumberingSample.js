// One last stop before the plan can be set into motion!
// It's up to you to help Senick get the average size of these yetis.

// Find all the Yetis using 'findByType':
var yetis = hero.findByType("yeti");
// Implement the averageSize function from scratch:
function avgSize(units) {
    if (units.length === 0)
        return 0;
    var total = 0;
    for (var i = 0; i < units.length; i++) {
        total += units[i].size;
    }
    return total / units.length;
}
// Say the average size of the yetis:
hero.say(avgSize(yetis));
