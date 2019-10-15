targets = []
targets.append({ "x": hero.pos.x, "y": hero.pos.y - 5 })
targets.append({ "x": hero.pos.x, "y": hero.pos.y + 5 });
targets.append({ "x": hero.pos.x - 5, "y": hero.pos.y });

while len(targets) > 0:
    if hero.isReady("throw"):
        target = targets.pop()
        hero.throwPos(target)
    else:
        hero.wait(0.01)
