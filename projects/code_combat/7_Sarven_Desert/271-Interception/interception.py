while True:
    enemy = hero.findNearestEnemy()
    friend = hero.findNearestFriend()
    hero.moveXY((friend.pos.x + enemy.pos.x) / 2, (friend.pos.y + enemy.pos.y) / 2);
