# Defeat the enemy hero in under three minutes.
    
def buildArmy():
    # Your hero can summon and command allied troops.
    
    # "archer", "artillery", "arrow-tower"
    buildOrder = ["soldier", "soldier", "soldier", "soldier", "soldier", "soldier", "soldier", "soldier", "soldier",
                  "soldier", "archer", "soldier", "archer", "soldier", "archer"]
    # "arrow-tower" "artillery"
    type = buildOrder[len(hero.built) % len(buildOrder)]
    if hero.gold >= hero.costOf(type):
        hero.summon(type)
    
def commandArmy():
    friends = hero.built
    enemies = hero.findEnemies()
    points = hero.getControlPoints()
    for i, friend in enumerate(friends):
        if friend.health <= 0 or friend.type == "arrow-tower":
            continue
        # Command your army to capture control points.
        # Make sure to choose your control points wisely!
        
        point = points[i % len(points)]
        if hero.time < 90:
            hero.command(friend, "defend", point.pos)
        else:
            enemies = self.findEnemies()
            nearestEnemy = self.findNearest(enemies)
            self.command(friend, "attack", nearestEnemy)


def attack(target):
    if target:
        if self.isReady("throw") and self.distanceTo(target) < self.throwRange:
            self.throw(target)
        elif (self.distanceTo(target) > 10):
            self.move(target.pos)
        elif (self.isReady("stomp") and self.distanceTo(target) < 5):
            self.stomp()
        elif (self.isReady("attack")):
            self.attack(target)

    
def controlHero():
    enemies = hero.findEnemies()
    nearestEnemy = hero.findNearest(enemies)
    shouldAttack = self.now() > 30
    if shouldAttack:
        attack(nearestEnemy)
    # Use your hero's abilities to turn the tide.
    # if shouldAttack: ...
    
    
while True:
    buildArmy()
    commandArmy()
    controlHero()
