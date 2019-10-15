// Protect the village with fire traps.
// Mine all passages in four directions.
// You have 80 seconds before the ogres attack.

// Build traps on the line y=114 from x=40 to x=112 with step=24.
function buildNorthLine() {
    for (var x = 40; x <= 112; x += 24) {
        hero.buildXY("fire-trap", x, 114);
    }
}

// Build traps on the line x=140 from y=110 to y=38 with step=18.
function buildEastLine() {
    // Complete this function:
    for (var y = 110; y >= 38; y -= 18) {
        hero.buildXY("fire-trap", 140, y);
    }
}

// Build traps on the line y=22 from x=132 to x=32 with step=20.
function buildSouthLine() {
    // Complete this function:
    for (var x = 132; x >= 32; x -= 20) {
        hero.buildXY("fire-trap", x, 22);
    }
}

// Build traps on the line x=20 from y=28 to y=108 with step=16.
function buildWestLine() {
    // Complete this function:
    for (var y = 28; y <= 108; y += 16) {
        hero.buildXY("fire-trap", 20, y);
    }
}

buildNorthLine();
buildEastLine();
buildSouthLine();
buildWestLine();
hero.moveXY(40, 94);
