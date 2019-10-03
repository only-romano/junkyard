// Defend against Brak and Treg!
// You must attack small ogres twice.

hero.attack("Brak");
hero.attack("Treg");
var item = hero.findNearestItem();
hero.moveXY(item.pos.x, item.pos.y);
