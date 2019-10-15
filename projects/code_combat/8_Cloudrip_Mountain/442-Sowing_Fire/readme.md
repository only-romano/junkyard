## _Sowing Fire_

#### _Legend says:_
> Plant a field of fire-traps while ogres try to explode you.

#### _Goals:_
+ _Plant three rows of nine fire trapss_
+ _No fire traps detonated_
+ _Retreat to the X_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](sowingFire.js)**
+ **[Python](sowing_fire.py)**

#### _Rewards:_
+ 386 xp
+ 178 gems

#### _Victory words:_
+ _DANGER: DO NOT REAP_

___

### _HINTS_

Build 3 columns of `"fire-trap"`s without letting any of the ogres through!

Follow the helper functions to set up the columns.

First, fill in the logic of the `cooseStrategy` function so that it returns the correct string according to the instructions in the comments.

Next, change the line that calculates `newY`. Use `(numTraps % trapsInColumn)` to make sure the function wraps around for each column of traps.

Finally, write the code for `commandAttack` and `commandRetreat`.

___
