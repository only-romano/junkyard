// If the ogre takes damage, she'll wake up and smash the peasant.
// You've got these razor-discs you can throw(). Maybe that'll help?
// Looks like you'll need three discs to defeat the ogre.
// Make all three hit the ogre simultaneously!
// Hint: razor discs bounce off of obstacles!

var targets = [];
targets.push({ x: hero.pos.x, y: hero.pos.y - 5 });
// Figure out where to throw the other two discs.
targets.push({ x: hero.pos.x, y: hero.pos.y + 5 });
targets.push({ x: hero.pos.x - 5, y: hero.pos.y });

while(targets.length > 0) {
    if(hero.isReady("throw")) {
        // shift() removes and returns the first element of an array
        var target = targets.shift();
        hero.throwPos(target);
    } else {
        hero.wait(0.01);
    }
}
