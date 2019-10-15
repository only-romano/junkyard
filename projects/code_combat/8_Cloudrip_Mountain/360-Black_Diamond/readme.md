## _Black Diamond_

#### _Legend says:_
> Avoid deadly mountain hazards as you scoop up gems on this difficult terrain.

#### _Goals:_
+ _Grab the gems_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/Else Statements**
+ **Nested If Statements**
+ **Object Literals**

#### _Solutions:_
+ **[JavaScript](blackDiamond.js)**
+ **[Python](black_diamond.py)**

#### _Rewards:_
+ 331 xp
+ 163 gems

#### _Victory words:_
+ _YOU'RE SMARTER THAN THE AVERAGE BEAR._

___

### _HINTS_

Use the `isPathClear` function to check for hazards between two points.

Only move to gems if the path is clear! Otherwise return to the center.

The sample code shows you how to use the `isPathClear` method to check if there is an open, hazard-free path in a straight line between two positions.

In this case, `clear` will be true if the path is clear between you and the nearest gem.

If `clear` is true, use `move` to move to `gem`'s `pos`.

If it's not true, use an object literal to `move` toward the center X mark at `40, 35`.

___
