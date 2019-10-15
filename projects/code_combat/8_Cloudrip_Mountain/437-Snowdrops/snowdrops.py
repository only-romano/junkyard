forestMap = hero.findNearest(hero.findFriends()).forestMap
hero.say("Row " + 0 + " Column " + 1 + " Fire!")
cells = [
    {"row": 0, "col": 4}, {"row": 1, "col": 0}, {"row": 1, "col": 2}, {"row": 1, "col": 4},
    {"row": 2, "col": 1}, {"row": 2, "col": 3}, {"row": 2, "col": 5}, {"row": 3, "col": 0},
    {"row": 3, "col": 2}, {"row": 3, "col": 4}, {"row": 4, "col": 1}, {"row": 4, "col": 2},
    {"row": 4, "col": 3}, {"row": 5, "col": 0}, {"row": 5, "col": 3}, {"row": 5, "col": 5},
    {"row": 6, "col": 1}, {"row": 6, "col": 3}, {"row": 6, "col": 4}, {"row": 7, "col": 0}]

for i in range(len(cells)):
    row = cells[i]["row"]
    col = cells[i]["col"]
    if row < forestMap.length and col < forestMap[row].length and forestMap[row][col] == 0:
        hero.say("Row " + row + " Column " + col + " Fire!")
