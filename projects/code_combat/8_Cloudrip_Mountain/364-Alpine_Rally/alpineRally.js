// Escape off the right side of the map.
// To outrun the  yeti, you'll have to make yourself faster.
// Use resetCooldown to use a spell or skill more frequently.
// manaBlast can help clear the path.

hero.cast("haste", hero);

while (true) {
    if (hero.pos.x > 100)
        hero.manaBlast();
    if (hero.pos.x > 150) {
        hero.resetCooldown("haste");
    }
    if (hero.canCast("haste"))
        hero.cast("haste", hero);
    hero.move({"x": 273, "y": 35});
}
