everybody = ['Yetu', 'Tabitha', 'Rasha', 'Max', 'Yazul',  'Todd']
enemyIndex = 0

while enemyIndex < everybody.length:
    ogre = everybody[enemyIndex]
    hero.attack(ogre)
    enemyIndex += 2

hero.moveXY(35, 54)
