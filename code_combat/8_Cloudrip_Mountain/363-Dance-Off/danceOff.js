// Move in sync with your dance partner to impress Pender Spellbane.

var partner = hero.findNearest(hero.findFriends());

var yDif = hero.pos.y - partner.pos.y;
var xDif = hero.pos.x - partner.pos.x;

while (true) {
    hero.move({"x": partner.pos.x + xDif, "y": partner.pos.y + yDif});
}
