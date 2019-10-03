var twoPi = 2 * Math.PI;

// Here are some functions for drawing shapes:
function degreesToRadians(degrees) {
    return (degrees/360)*twoPi;
}

function drawPolyStars(center, radius, sides, skips, startAngle) {
    hero.toggleFlowers(false);
    var angle = startAngle;
    var x = center.x;
    var y = center.y;
    var hoops = skips + 1;
    var stepAngle = hoops * (twoPi / sides);
    if(skips !== 0 && (sides % hoops) === 0) {
        hoops = skips;
    }
    var endAngle = (twoPi * hoops) + startAngle;
    while(angle <= endAngle) {
        var newX = x + radius * Math.cos(angle);
        var newY = y + radius * Math.sin(angle);
        hero.moveXY(newX, newY);
        hero.toggleFlowers(true);
        angle += stepAngle;
    }
}

function drawStar(center, radius, sides, skips, startAngle) {
    var skipsPlusOne = skips + 1;
    if ((sides/skipsPlusOne) != 1 && (sides%skipsPlusOne) === 0) {
        var index = skips;
        while(index >= 0) {
            var angle = startAngle + index * (twoPi / sides);
            drawPolyStars(center, radius, sides, skips, angle);
            index -= 1;
        }
    } else {
        drawPolyStars(center, radius, sides, skips, startAngle);
    }
}

function drawPolygon(center, radius, sides, startAngle) {
    drawPolyStars(center, radius, sides, 0, startAngle);
}

function drawSpokes(center, radius, sides, startAngle) {
    var x = center.x;
    var y = center.y;
    var endAngle = twoPi + startAngle;
    var stepAngle = twoPi / sides;
    var angle = startAngle;
    while(angle < endAngle) {
        var newX = x + radius * Math.cos(angle);
        var newY = y + radius * Math.sin(angle);
        if((hero.pos.x|0) == (x|0) && (hero.pos.y|0) == (y|0)) {
            hero.toggleFlowers(true);
            hero.moveXY(newX, newY);
        } else {
            hero.toggleFlowers(false);
            hero.moveXY(newX, newY);
            hero.toggleFlowers(true);
            hero.moveXY(x, y);
        }
        hero.toggleFlowers(false);
        angle += stepAngle;
    }
}

function drawSpiral(center, size, loopNum, startAngle) {
    var newX, x = center.x;
    var newY, y = center.y;
    hero.toggleFlowers(false);
    hero.moveXY(x, y);
    hero.toggleFlowers(true);
    var steps = size * 2;
    var direction = Math.sign(loopNum);
    var stepAngle = twoPi / steps / direction;
    var loops = direction * loopNum;
    var stepSize = size / steps / loops;
    var curSize = 0;
    var angle = startAngle;
    var endAngle = (twoPi * loopNum) + startAngle;
    while(loopNum<0 ? (angle>=endAngle) : (angle<=endAngle)) {
        newX = x + curSize * Math.cos(angle);
        newY = y + curSize * Math.sin(angle);
        hero.moveXY(newX, newY);
        angle += stepAngle;
        curSize += stepSize;
    }
    newX = x + size * Math.cos(endAngle);
    newY = y + size * Math.sin(endAngle);
    hero.moveXY(newX, newY);
}

var redX = {x: 28, y: 36};
var whiteX = {x: 60, y: 36};

// --------------------------------------------------
//setFlowerColor
hero.setFlowerColor("red");
// Draw a "3D style" box, using the drawPolygon and drawSpokes functions, centered on the red X and with a size of 10.
// The simplest startAngles to calculate would be either "up" or "down".
// The drawing functions deal with angles in terms of radians. If you think in terms of degrees then please use the "degreesToRadians(degrees)" function so they can understand you.
//drawPolygon(center, size, number of sides, start angle)
drawPolygon({x: 28, y: 36}, 10, 6, twoPi / 4);
//drawSpokes(center, size, number of spokes, start angle)
drawSpokes({x: 28, y: 36}, 10, 3, twoPi / 4 * 3);

// Draw the star bib, using the drawStar and drawSpiral functions. (See the Guide for an image of the shapes.)
// The star is centered on the white X and has a size of 6.
// The spirals have a size of 15. To get a spiral to go the other direction give it a negative number of loops.
//setFlowerColor
hero.setFlowerColor("white");
//drawStar(center, size, sides, skips, startAngle)
drawStar({x: 60, y: 36}, 6, 7, 2, twoPi / 4);
//setFlowerColor
hero.setFlowerColor("pink");

//drawSpiral(center, size,  number of loops, start angle)
drawSpiral({x: 60, y: 42}, 15,  1, twoPi / 4 * 3);

//drawSpiral(center, size,  number of loops, start angle)
drawSpiral({x: 60, y: 42}, 15,  -1, twoPi / 4 * 3);
