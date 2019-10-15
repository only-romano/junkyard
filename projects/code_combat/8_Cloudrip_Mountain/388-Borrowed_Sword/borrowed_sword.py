def strongestEnemy(enemies):
    strongest = None
    health = 0
    for enemy in enemies:
        if enemy.health > health:
            health = enemy.health
            strongest = enemy
    return strongest


while True:
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    target = strongestEnemy(enemies)
    if target:
        for friend in friends:
            hero.command(friend, "attack", target)
