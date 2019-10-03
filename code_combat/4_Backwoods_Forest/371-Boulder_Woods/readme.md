## _Boulder Woods_

#### _Legend says:_
> Navigate around boulders to reach your goal.

#### _Goals:_
+ _Reach the end marker_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Accessing Properties**
+ **Geometry**
+ **Vectors**

#### _Solutions:_
+ **[JavaScript](boulderWoods.js)**
+ **[Python](boulder_woods.py)**

#### _Rewards:_
+ 337 xp
+ 165 gems

#### _Victory words:_
+ _THE BOULDER IS NOT AMUSED_

___

### _HINTS_

This level introduces `isPathClear(start,end)`.

`isPathClear` will return `true` if the path is clear between `start` and `end`, otherwise it returns `false`.

Start and end are `{x,y}` position objects.

For this level, the pathfinding math has been given to you - all you need to do is use an `if/else` statement with `isPathClear`.

If the path is clear, you should use `move` to move toward the target. If it's not clear, use the `angle -= Math.PI / 16` line to adjust the angle.

___
