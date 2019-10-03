// You MUST click on the HELP button to see a detailed description of this level!

// The raven will tell you what to use for your maze parameters!
var helpSlide = 9;
var helpSwitch = 5;
var helpSkip = 7;
// How many sideSteps north of the Red X you've taken.
var sideSteps = 1;

// How many steps east of the Red X you've taken.
var steps = 1;

// Multiply this with steps to determine your X coordinate. DON'T CHANGE THIS!
var X_PACE_LENGTH = 4;

// Multiply this with sideSteps to determine your Y coordinate. DON'T CHANGE THIS!
var Y_PACE_LENGTH = 6;

var sideSwitcher = true;
// The maze is 35 steps along the X axis.
while(steps <= 35) {
    // Take the next step:
    if (sideSteps > helpSlide) {
        sideSteps = 1;
    } else if (sideSteps < 1) {
        sideSteps = helpSlide;
    }
    hero.moveXY(steps * X_PACE_LENGTH, sideSteps * Y_PACE_LENGTH);

    // Increment steps and sideSteps as appropriate, taking into account the special rules.
    if (steps % helpSwitch === 0) {
        sideSwitcher = !sideSwitcher;
    }
    if (sideSwitcher) {
        sideSteps++;
    } else {
        sideSteps--;
    } 
    if (steps % helpSkip === 0) {
        if (sideSwitcher) {
            sideSteps++;
        } else {
            sideSteps--;
        }
    }
    steps++;
}
