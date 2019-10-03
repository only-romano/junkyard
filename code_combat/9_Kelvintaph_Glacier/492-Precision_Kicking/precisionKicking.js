// Push the ball to knock over all the blue skeletons without hitting any red ones.
// The blue skeletons can be found as enemies.
var center = Vector(40, 35);
var punch_array = [];
var enemies = hero.findEnemies();
var friend = hero.findFriends()[0];
var ball = hero.findNearest(hero.findByType('ball'));
var ballPos = Vector(ball.pos.x, ball.pos.y);
for (var i = 0; i < enemies.length; i++) {
    var enemy = enemies[i];
    var s2b = Vector.multiply(Vector.normalize(Vector.subtract(ballPos, enemy.pos)), 7);
    var b2p = ball.pos.add(s2b);
    punch_array.push(b2p);
}

var distance = 100;
while (punch_array.length > 0) {
    var min_dist = 200;
    var min_index = -1;
    for (var i = 0; i < punch_array.length; i++) {
        var punch = punch_array[i];
        if (min_dist > Vector.subtract(punch, friend.pos).magnitude()) {
            min_dist = Vector.subtract(punch, friend.pos).magnitude();
            min_index = i;
        }
    }
    var vector = punch_array.splice(min_index, 1)[0];
    hero.command(friend, 'move', vector);
    hero.wait(1);
    hero.command(friend, 'move', center);
    hero.wait(1);
    hero.command(friend, 'move', vector);
}
