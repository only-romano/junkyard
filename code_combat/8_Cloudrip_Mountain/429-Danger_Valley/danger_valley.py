for i in range(len(hero.grid)):
    row = hero.grid[i]
    for j in range(len(row)):
        if row[j] == 1:
            hero.buildXY("fire-trap", 36 + 6 * j, 20 + 6 * i)

hero.moveXY(29, 56)
