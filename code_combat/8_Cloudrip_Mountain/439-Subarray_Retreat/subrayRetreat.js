// Find the subarray of gems with the best summary value.

// This function solves the problem in linear time.
function dynamicMaxSum (gems) {
    var cycles = 0;
    var maxStartIndex = 0;
    var maxEndIndex = 0;
    var maxEndHere = 0;
    var currentStartIndex = 0;
    var maxBest = 0;
    for (var i = 0; i < gems.length; i++) {
        cycles++;
        maxEndHere += gems[i].value;
        if (maxEndHere < 0) {
            maxEndHere = 0;
            currentStartIndex = i + 1;
        }
        if (maxEndHere > maxBest) {
            maxStartIndex = currentStartIndex;
            maxEndIndex = i;
            maxBest = maxEndHere;
        }
    }
    hero.say("I's taken " + cycles + " cycles.");
    return [maxStartIndex, maxEndIndex];
}

// This function solves the problem in quadratic time.
function naiveMaxSum(gems) {
    var cycles = 0;
    var maxStartIndex = 0;
    var maxEndIndex = 0;
    var maxBest = 0;
    for (var i = 0; i < gems.length; i++) {
        var sum = 0;
        for (var j = i; j < gems.length; j++) {
            cycles++;
            if (cycles > 104) {
                hero.say("I fed up of calculations.");
                return [i, j];
            }
            sum += gems[j].value;
            if (sum > maxBest) {
                maxStartIndex = i;
                maxEndIndex = j;
                maxBest = sum;
            }
        }
    }
    hero.say("I's taken " + cycles + " cycles.");
    return [maxStartIndex, maxEndIndex];
}

// Don't worry "findItems" sort out gems by X coordinate.
var items = hero.findItems();
var edges = naiveMaxSum(items);

var x1 = edges[0] * 4 + 4;
var x2 = edges[1] * 4 + 4;

// Collect gems from x1 to x2 and escape:
hero.moveXY(x1, 40);
hero.moveXY(x2, 40);
hero.moveXY(40,64);
