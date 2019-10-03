fencePrice = 3
lawnPrice = 2
foreman = hero.findNearest(hero.findFriends())
corners = foreman.corners
bottomLeft = corners.bottomLeft
topRight = corners.topRight
width = topRight.x - bottomLeft.x
height = topRight.y - bottomLeft.y
perimeter = 2 * (width + height)
fence = perimeter * fencePrice
area = width * height
lawn = area * lawnPrice
totalCost = fence + lawn
hero.say("The total price is " + totalCost)
foreman.bill(totalCost)
