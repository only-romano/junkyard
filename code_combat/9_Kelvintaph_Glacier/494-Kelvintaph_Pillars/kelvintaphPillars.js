// Move the stack of peasants onto another stump.
// You can only carry 1 peasant at a time.
// You cannot stack a larger peasant onto a smaller peasant.
// You have access to the following APIs:
// pickUpItem(container) picks up the top/last item in a container.
// dropItem(container) drops the top/last (and only) item in you're carrying.
// You and the stumps have the following APIs:
// peekItem() returns the top item of the container.
// viewStack() returns an array of items in the container.
// Peasants have the following APIs:
// size; returns the size of the peasant

function findMax(stack) {
    var maxSize = 0;
    var max = null;
    for (var i = 0; i < stack.length; i++) {
        var peasant = stack[i];
        if (peasant.size > maxSize) {
            maxSize = peasant.size;
            max = peasant;
        }
    }

    return max;
}

function isEmpty(stack) {
    return stack.viewStack().length === 0;
}


function movePeasant(from, to) {
    hero.pickUpItem(from);
    hero.dropItem(to);
}


function moveNextItem(s1, s2, s3) {
    var item = s1.peekItem();
    if (item == findMax(s1.viewStack().concat(s2.viewStack())))
        movePeasant(s1, s3);
    else
        movePeasant(s1, s2);
}


var stump1 = hero.findByType('stump')[0]; // This is where the peasants start.
var stump2 = hero.findByType('stump')[1];
var stump3 = hero.findByType('stump')[2];

while (!isEmpty(stump1) || !isEmpty(stump2)) {
    while (!isEmpty(stump1))
        moveNextItem(stump1, stump2, stump3);
    while (!isEmpty(stump2))
        moveNextItem(stump2, stump1, stump3);
}
