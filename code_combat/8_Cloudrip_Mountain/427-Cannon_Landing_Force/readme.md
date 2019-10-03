## _Cannon Landing Force_

#### _Legend says:_
> How to get over high mountains? Ride a cannonball.

#### _Goals:_
+ _Land 3 soldiers_
+ _Destroy the fire-traps_

#### _Topics:_
+ **Basic Syntax**
+ **Strings**
+ **Variables**
+ **Array Indexes**
+ **2D Array**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](cannonLandingForce.js)**
+ **[Python](cannon_landing_force.py)**

#### _Rewards:_
+ 385 xp
+ 144 gems

#### _Victory words:_
+ _MAYBE WE SHOULD GIVE THE SOLDIERS PARACHUTES?_

___

### _HINTS_

Frontier colonists need our help and we can send some soldiers to the mountain village. Also they asked to clear the square from old fire traps. How will we do it? With cannons of course!

The artillery can launch soliers and anti-trap shell over mountains. Peasants meet us on the square, so be careful to launch soldiers.

We have a map as a 2 dimensional array (a grid), so you can get the values of the specific cells.

___

The map of the square is represented as a 2-dimensional array (a grid) with string values. The 2-dimensional array is an array where each element is an array. As the result, we get something like a spreadsheet. Arrays inside can have various lengths, but for our case, they all have the same length. Usually, if you use 2d arrays to represent a spreadsheet or a map it's useful to use the same length for each row.

2d array can be written this way:

```javascript
var grid = [[0, 1, 2],
            [3, 4, 5]];
```

In the above example the grid contains 2 rows and 3 columns. If we need to get the value of specific elements we can use the next syntax (don't forget the first row has the index 0):

```javascript
// get the first element
grid[0][0];  // it's 0
// the last element
grid[1][2];  // it's 5
// the row 1 the column 0
grid[1][0];  // 3
```

The map of the town square on this level is represented as a 2d array of strings. Each cell contain the string value: "peasant", "trap" or "clear".

For example (the level grid can have another size):

```javascript
var landingMap = [
    ["peasant", "clear", "clear", "trap"],
    ["trap", "clear", "peasant", "peasant"],
    ["clear" "trap", "clear", "clear"]];
```

Rows and columns are counted from zero in the directions as X and Y coordinates. To shoot the cannons need to know grid coordinates (the row and the column) and what in that cell is.

So if you need to shoot at the row 2 and the column 3, then first get the value at that cell and say this:

```javascript
var cellValue = landingMap[2][3];  // clear
hero.say("Row 2 column 3 - " + cellValue);
```

If the cannons hear "trap" or "clear" in your commands, then one of them (depends on the type) shoots. Be careful and give only correct coordinates. For example, if the grid's size is 3x4:

```javascript
// Wrong coordinaes for the cannon. BOOM!
hero.say("Row 9001 column 19 - " + landingMap[2][3]);
// Wrong indexes to access. ReferenceError.
hero.say("Row 2 column 3 - " + landingMap[9001][19]);
```
Use cell coordinates that are given in the sample code to be sure for the success.

___
