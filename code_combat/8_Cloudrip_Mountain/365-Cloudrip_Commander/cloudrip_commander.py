while hero.gold > hero.costOf("soldier"):
    hero.summon("soldier")
    
soldiers = hero.findFriends()
for soldier in soldiers:
    hero.command(soldier, "move", {x: 50, y: 40})

while hero.pos.x < 50:
    hero.move({"x": 50, "y": 40})
