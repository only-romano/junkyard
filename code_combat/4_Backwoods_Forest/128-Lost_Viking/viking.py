helpSlide = 9
helpSwitch = 5
helpSkip = 7
sideSteps = 1
steps = 1
X_PACE_LENGTH = 4
Y_PACE_LENGTH = 6
sideSwitcher = True

while steps <= 35:
    if sideSteps > helpSlide:
        sideSteps = 1
    else if sideSteps < 1:
        sideSteps = helpSlide
    
    hero.moveXY(steps * X_PACE_LENGTH, sideSteps * Y_PACE_LENGTH)

    if steps % helpSwitch == 0:
        sideSwitcher = !sideSwitcher

    if sideSwitcher:
        sideSteps += 1
    else:
        sideSteps -= 1

    if steps % helpSkip == 0:
        if sideSwitcher:
            sideSteps += 1
        else:
            sideSteps -= 1

    steps += 1
