## _Power Points_

#### _Legend says:_
> Only true wizards can see the points of the Power. Or you can buy the map from one of wizards.

#### _Goals:_
+ _Find and defeat the skeletons_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](powerPoints.js)** _warrior_
+ **[Python](power_points.py)** _wizard_

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _NOW, ONTO THE NEXT SLIDE._

___

### _HINTS_

To pass the trial you must defeat 3 dark creatures. But first, you need to find them. To summon a skeleton or something useful you should stay on a point of the Power and _say "VENI"_.

But there are too many possible points and if the spell is said in the wrong place, then it can be bad (for you). Only wizards can see the points of the Power. Luckily you know one of them and he prepared the map for you.

The map is represented as a 2-dimensional array (grid) of numbers. `0` is a wrong place. Positive numbers are power points. Iterate through the grid, find the points and meet your challenges.

___

The map that we get from the wizard is a 2-dimensional array of numbers. It's an array where each element is an array of number. It looks like this:

```javascript
var powerMap = [
    [0, 1, 0, 0, 0],
    [2, 0, 0, 3, 0],
    [0, 0, 4, 0, 0],
    [0, 0, 0, 0, 5]];
```

To iterate all elements from that arrays we need to use two concepts from the previous levels: nested loops and 2d array elements reading.

First we should iterate all elements of the root array which are arrays too:

```javascript
for (var i = 0; i < powerMap.length; i++) {
    // ...
}
```

Next, use the nested loop to iterate through each array. You can save get a row inside the loop definition or save it in a variable for the each inner loop. As the result we have values of the row and the column for all elements and can get their value:

```javascript
for (var i = 0; i < powerMap.length; i++) {
    for (var j = 0; j < powerMap[i].length; j++) {
        var value = powerMap[i][j];
    }
}
```

___
