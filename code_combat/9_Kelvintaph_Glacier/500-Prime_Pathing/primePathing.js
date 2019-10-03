// Get all your troops to the end of the path by passing over the mines.
// You can locate duds by finding the mines that have a value that is a prime number.
// Check the guide for clarification.

function primeCheck(number) {
    var end = Math.sqrt(number);
    for (var i = 2; i < end; i++)
        if (number % i === 0)
            return false;
    return true;
}

function passMines(mines) {
    for (var i = 0; i < mines.length; i++) {
        var mine = mines[i];
        if (primeCheck(mine.value))
            return mine;
    }
    return null;
}

function getWay(mine, direction) {
    var way = [];
    if (direction == "west") {
        way.push({"x": mine.pos.x + 7, "y": mine.pos.y});
        way.push({"x": mine.pos.x - 7, "y": mine.pos.y});
    }
    else if (direction == "east") {
        way.push({"x": mine.pos.x - 7, "y": mine.pos.y});
        way.push({"x": mine.pos.x + 7, "y": mine.pos.y});
    }
    else if (direction == "north") {
        way.push({"x": mine.pos.x, "y": mine.pos.y - 7});
        way.push({"x": mine.pos.x, "y": mine.pos.y + 7});
    }
    return way;
}

function findMines(x1, x2, y1, y2) {
    var mines = hero.findHazards();
    var result = [];
    for (var i = 0; i < mines.length; i++) {
        var mine = mines[i];
        var pos = mine.pos;
        if (pos.x > x1 && pos.x < x2 && pos.y > y1 && pos.y < y2)
            result.push(mine);
    }
    return result;
}

function moveTheWay(x1, x2, y1, y2, direction) {
    var mines = findMines(x1, x2, y1, y2);
    var mine = passMines(mines);
    if (mine) {
        var way = getWay(mine, direction);
        hero.moveXY(way[0].x, way[0].y);
        hero.moveXY(way[1].x, way[1].y);
        return way;
    }
}

function commandUnits(way, friends) {
    moveUnits(way[0], friends);
    moveUnits(way[1], friends);
}

function moveUnits(pos, friends) {
    for (var i = 0; i < friends.length; i++) {
        hero.command(friends[i], "move", pos);
    }
    hero.wait(1.5);
}

var friends = hero.findFriends();
var route = [];
commandUnits(moveTheWay(56, 63, 25, 50, "west"), friends);
commandUnits(moveTheWay(33, 45, 25, 50, "west"), friends);
commandUnits(moveTheWay(14, 24, 25, 50, "west"), friends);
moveUnits({"x": 5, "y": 10}, friends);
hero.moveXY(5, 10);
commandUnits(moveTheWay(5, 15, 0, 20, "east"), friends);
commandUnits(moveTheWay(25, 35, 0, 20, "east"), friends);
commandUnits(moveTheWay(45, 55, 0, 20, "east"), friends);
commandUnits(moveTheWay(65, 75, 0, 20, "east"), friends);
moveUnits({"x": 90, "y": 10}, friends);
hero.moveXY(90, 10);
commandUnits(moveTheWay(80, 105, 10, 25, "north"), friends);
commandUnits(moveTheWay(80, 105, 25, 40, "north"), friends);
commandUnits(moveTheWay(80, 105, 40, 55, "north"), friends);
