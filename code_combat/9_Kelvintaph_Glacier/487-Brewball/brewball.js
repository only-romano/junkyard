// Say anything within 10m of Omarn for him to throw a potion.
// Catch the potion by standing near it before it lands.
// DO NOT LET THE POTION LAND ON THE GROUND!

function avoidNearest(target) {
    var nearest = hero.findNearest(firetraps);
    var tarWay = Vector.subtract(target, hero.pos);
    var nearWay = Vector.subtract(nearest.pos, hero.pos);
    if (hero.distanceTo(nearest) > 4) {
        var step = Vector.normalize(tarWay);
        var newPos = Vector.add(hero.pos, step);
        hero.moveXY(newPos.x, newPos.y);
        return;
    }
    var angle1 = Vector.heading(tarWay);
    var angle2 = Vector.heading(nearWay);

    if (target.x < nearest.pos.x) {
        angle1 = - angle1;
        angle2 = - angle2;
        angle1 = Math.PI - angle1;
        angle2 = Math.PI - angle2;
    }
    var adVec;
    if (angle1 > angle2)
        adVec = Vector.rotate(nearWay, Math.PI / 2);
    else
        adVec = Vector.rotate(nearWay, - Math.PI / 2);
    var newPos = Vector.add(hero.pos, adVec);
    hero.moveXY(newPos.x, newPos.y);
}


while(true) {
    var potion = hero.findFriendlyMissiles()[0];
    var firetraps = hero.findHazards();
    // Remember that a Fire Trap will trigger if you move closer than 3 meters!
    var omarn = hero.findByType("potion-master")[0];
    if(potion) {
        var dest = potion.targetPos;
        // Go get the potion.
        avoidNearest(dest);
        // Warning: isPathClear doesn't work with Hazards!
    } else {
        if(omarn && hero.distanceTo(omarn) > 10) {
            // Move back to Omarn.
            avoidNearest(omarn.pos);
        } else {
            hero.say("Hup, hup!");
        }
    }
}
