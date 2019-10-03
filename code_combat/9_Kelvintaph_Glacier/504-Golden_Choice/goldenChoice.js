// You must collect the required amount of gold.
// The gate keeper will tell you how much you need.
// Always move in the direction of the exit.
// For each row you can take only one coin.
// Choose only one from the nearest coins in the next row.

// ! SEE PYTHON SOLUTION !

// Distance between rows and coins.
var distanceX = 4;
var distanceY = 6;
var zeroPoint = {x: 14, y: 14};
var coinLines = 10;

function makeGoldMap(coins) {
    var template = [];
    for (var i = 0; i < coinLines; i++) {
        template[i] = [];
        for (var j = 0; j < 2 * coinLines - 1; j++) {
            template[i][j] = 0;
        }
    }
    for (var c = 0; c < coins.length; c++) {
        var row = Math.floor((coins[c].pos.y - zeroPoint.y) / distanceY);
        var col = Math.floor((coins[c].pos.x - zeroPoint.x) / distanceX);
        template[row][col] = coins[c].value;
    }
    return template;
}

// Prepare the gold map. It looks like:
// [[1, 0, 9, 0, 4],
//  [0, 1, 0, 9, 0],
//  [8, 0, 2, 0, 9]]
var goldMap = makeGoldMap(hero.findItems());

// Find your path.
