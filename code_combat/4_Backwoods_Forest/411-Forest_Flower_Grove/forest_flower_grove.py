from math import pi, sin, cos

def circle(angle, condition, step):
    angle = pi * angle
    while angle < pi * condition:
        hero.moveXY(hero.pos.x + cos(angle),hero.pos.y + sin(angle))
        angle += pi / step


circle(0.5, 1.5, 96)
circle(1.5, 2.5, 124)
circle(0.5, 1.5, 96)
circle(1.5, 20, 68)
