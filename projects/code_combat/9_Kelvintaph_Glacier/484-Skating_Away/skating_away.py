goalPoint = new Vector(78, 34)

while True:
    goal = Vector.multiply(Vector.normalize(Vector.subtract(goalPoint, hero.pos)), 10)
    yak = hero.findNearest(hero.findEnemies());
    if(hero.distanceTo(yak) < 10) {
        way = Vector.multiply(Vector.normalize(Vector.subtract(hero.pos, yak.pos)), 10)
        goal = Vector.add(goal, way)
    }
    hero.move(Vector.add(hero.pos, goal))
