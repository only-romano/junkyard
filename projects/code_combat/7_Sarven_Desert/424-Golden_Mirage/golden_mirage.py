while True:
    coins = hero.findItems()
    unique = None
    for i in range(len(coins)):
        unique = coins[i]
        for j in range(len(coins)):
            if i == j:
                continue
            if coins[i].value == coins[j].value:
                unique = None
                break
        if unique:
            break
    if unique:
        hero.moveXY(unique.pos.x, unique.pos.y)
