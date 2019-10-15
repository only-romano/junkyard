# Escape from the minefield.
# You need to pass the marked line. (x = 72).

trapDistance = 6
trapRange = 2

# Jump, Jump, JUMP!!!
jump = ['up', 'up', 'up', 'up', 'right', 'right', 'right', 'down', 'down','left', 'down', 'down', 'right', 'right', 'right', 'right']
index =  0
# Jump, Jump, JUMP!!!
while index<len(jump):
    if(hero.isReady('jump')):
        if jump[index]=='right':
            where = {'x': (hero.pos.x +(trapDistance)*2), 'y':hero.pos.y}
        elif jump[index]=='left':
            where = {'x': (hero.pos.x -(trapDistance)*2), 'y':hero.pos.y}
        elif jump[index]=='up':
            where = {'x': hero.pos.x, 'y':(hero.pos.y +(trapDistance)*2)}
        else:
            where = {'x': hero.pos.x, 'y':(hero.pos.y - (trapDistance)*2)}
        hero.jumpTo(where)
        index = index +  1
    else:
        hero.move(where)